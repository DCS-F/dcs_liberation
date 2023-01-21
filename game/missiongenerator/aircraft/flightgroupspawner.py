import copy
import logging
import random
from typing import Any, Union, Tuple, Optional

from dcs import Mission, Point
from dcs.country import Country
from dcs.mapping import Vector2
from dcs.mission import StartType as DcsStartType
from dcs.planes import F_14A, Su_33, AV8BNA, M_2000C, FA_18C_hornet
from dcs.point import PointAction
from dcs.ships import KUZNECOW
from dcs.terrain import Airport, NoParkingSlotError
from dcs.unitgroup import FlyingGroup, ShipGroup, StaticGroup
from dcs.weapons_data import Weapons

from game.ato import Flight
from game.ato.flightstate import InFlight
from game.ato.loadouts import Loadout
from game.ato.starttype import StartType
from game.ato.traveltime import GroundSpeed
from game.data.weapons import Weapon
from game.naming import namegen
from game.theater import Airfield, ControlPoint, Fob, NavalControlPoint, OffMapSpawn
from game.utils import feet, meters
from pydcs_extensions.a4ec.a4ec import A_4E_C

WARM_START_HELI_ALT = meters(1200)
WARM_START_ALTITUDE = meters(3000)

# In-flight spawns are MSL for the first waypoint (this can maybe be changed to AGL, but
# AGL waypoints have different piloting behavior, so we need to check whether that's
# safe to do first), so spawn them high enough that they're unlikely to be near (or
# under) the ground, or any nearby obstacles. The highest airfield in DCS is Kerman in
# PG at 5700ft. This could still be too low if there are tall obstacles near the
# airfield, but the lowest we can push this the better to avoid spawning helicopters
# well above the altitude for WP1.
MINIMUM_MID_MISSION_SPAWN_ALTITUDE_MSL = meters(3000)
MINIMUM_MID_MISSION_SPAWN_ALTITUDE_AGL = feet(500)

RTB_ALTITUDE = meters(800)
RTB_DISTANCE = 5000
HELI_ALT = meters(500)
F18_TGP_PYLON: int = 4


class FlightGroupSpawner:
    def __init__(
        self,
        flight: Flight,
        country: Country,
        mission: Mission,
        helipads: dict[ControlPoint, list[StaticGroup]],
        stol_pads_roadbase: dict[ControlPoint, list[Tuple[StaticGroup, Point]]],
        stol_pads: dict[ControlPoint, list[Tuple[StaticGroup, Point]]],
    ) -> None:
        self.flight = flight
        self.country = country
        self.mission = mission
        self.helipads = helipads
        self.stol_pads_roadbase = stol_pads_roadbase
        self.stol_pads = stol_pads

    def create_flight_group(self) -> FlyingGroup[Any]:
        """Creates the group for the flight and adds it to the mission.

        Each flight is spawned according to its FlightState at the time of mission
        generation. Aircraft that are WaitingForStart will be set up based on their
        StartType with a delay. Note that delays are actually created during waypoint
        generation.

        Aircraft that are *not* WaitingForStart will be spawned in their current state.
        We cannot spawn aircraft mid-taxi, so when the simulated state is near the end
        of a long taxi period the aircraft will be spawned in their parking spot. This
        could lead to problems but that's what loiter points are for. The other pre-
        flight states have the same problem but are much shorter and more easily covered
        by the loiter time. Player flights that are spawned near the end of their cold
        start have the biggest problem but players are able to cut corners to make up
        for lost time.

        Aircraft that are already in the air will be spawned at their estimated
        location, speed, and altitude based on their flight plan.
        """
        if (
            self.flight.state.is_waiting_for_start
            or self.flight.state.spawn_type is not StartType.IN_FLIGHT
        ):
            return self.generate_flight_at_departure()
        return self.generate_mid_mission()

    def create_idle_aircraft(self) -> FlyingGroup[Any]:
        assert isinstance(self.flight.squadron.location, Airfield)
        group = self._generate_at_airfield(
            name=namegen.next_aircraft_name(self.country, self.flight),
            airfield=self.flight.squadron.location,
        )

        group.uncontrolled = True
        return group

    @property
    def start_type(self) -> StartType:
        return self.flight.state.spawn_type

    def generate_flight_at_departure(self) -> FlyingGroup[Any]:
        name = namegen.next_aircraft_name(self.country, self.flight)
        cp = self.flight.departure

        is_f18 = self.flight.squadron.aircraft.dcs_unit_type.id == FA_18C_hornet.id
        on_land = not self.flight.squadron.location.is_fleet
        if is_f18:
            try:
                print(f"Before: {self.flight.loadout.pylons[F18_TGP_PYLON]}")

                if (
                    on_land
                    and self.flight.squadron.coalition.game.settings.atflir_autoswap
                ):
                    self.flight.loadout.pylons[F18_TGP_PYLON] = Weapon.with_clsid(  # type: ignore
                        str(
                            FA_18C_hornet.Pylon4.AN_AAQ_28_LITENING___Targeting_Pod_[1][
                                "clsid"
                            ]
                        )
                    )
                elif (
                    not on_land
                    and self.flight.squadron.coalition.game.settings.atflir_autoswap
                ):
                    self.flight.loadout.pylons[F18_TGP_PYLON] = Weapon.with_clsid(  # type: ignore
                        str(
                            FA_18C_hornet.Pylon4.AN_ASQ_228_ATFLIR___Targeting_Pod[1][
                                "clsid"
                            ]
                        )
                    )
                print(f"After: {self.flight.loadout.pylons[F18_TGP_PYLON]}")

            except KeyError:
                logging.warning(
                    f"Could not swap ATFLIR/LITENING for {self.flight.squadron.aircraft} {self.flight.flight_type} {self.flight.targets}"
                )

        try:
            if self.start_type is StartType.IN_FLIGHT:
                group = self._generate_over_departure(name, cp)
                return group
            elif isinstance(cp, NavalControlPoint):
                group_name = cp.get_carrier_group_name()
                carrier_group = self.mission.find_group(group_name)
                if not isinstance(carrier_group, ShipGroup):
                    raise RuntimeError(
                        f"Carrier group {carrier_group} is a "
                        f"{carrier_group.__class__.__name__}, expected a ShipGroup"
                    )
                return self._generate_at_group(name, carrier_group)
            elif isinstance(cp, Fob):
                if cp.has_helipads and (
                    self.flight.unit_type.helicopter
                    or self.flight.unit_type.dcs_unit_type in [AV8BNA]
                ):
                    pad_group = self._generate_at_cp_helipad(name, cp)
                    if pad_group is not None:
                        return pad_group
                if cp.has_stol_slots and (
                    self.flight.client_count > 0 or self.flight.unit_type.helicopter
                ):
                    pad_group = self._generate_at_cp_stol(name, cp)
                    if pad_group is not None:
                        return pad_group
                return self._generate_over_departure(name, cp)
            elif isinstance(cp, Airfield):
                if cp.has_helipads and self.flight.unit_type.helicopter:
                    pad_group = self._generate_at_cp_helipad(name, cp)
                    if pad_group is not None:
                        return pad_group
                if (
                    cp.has_stol_slots
                    and len(self.stol_pads[cp]) + len(self.stol_pads_roadbase[cp])
                    >= self.flight.count
                    and (
                        self.flight.client_count > 0 or self.flight.unit_type.helicopter
                    )
                ):
                    pad_group = self._generate_at_cp_stol(name, cp)
                    if pad_group is not None:
                        return pad_group
                # FlightGroupSpawner will now always air-start AI A-4E Skyhawks
                # because the AI is really bad at taking off with heavier loadouts.
                if (
                    self.flight.client_count < 1
                    and self.flight.unit_type.dcs_unit_type in [A_4E_C]
                ):
                    return self._generate_over_departure(name, cp)
                return self._generate_at_airfield(name, cp)

            if isinstance(cp, OffMapSpawn):
                return self._generate_over_departure(name, cp)
            else:
                raise NotImplementedError(
                    f"Aircraft spawn behavior not implemented for {cp} ({cp.__class__})"
                )
        except NoParkingSlotError:
            # Generated when there is no place on Runway or on Parking Slots
            logging.warning(
                "No room on runway or parking slots. Starting from the air."
            )
            group = self._generate_over_departure(name, cp)
            group.points[0].alt = 1500
            return group

    def generate_mid_mission(self) -> FlyingGroup[Any]:
        assert isinstance(self.flight.state, InFlight)
        name = namegen.next_aircraft_name(self.country, self.flight)
        speed = self.flight.state.estimate_speed()
        pos = self.flight.state.estimate_position()
        pos += Vector2(random.randint(100, 1000), random.randint(100, 1000))
        alt, alt_type = self.flight.state.estimate_altitude()

        # We don't know where the ground is, so just make sure that any aircraft
        # spawning at an MSL altitude is spawned at some minimum altitude.
        # https://github.com/dcs-liberation/dcs_liberation/issues/1941
        if alt_type == "BARO" and alt < MINIMUM_MID_MISSION_SPAWN_ALTITUDE_MSL:
            alt = MINIMUM_MID_MISSION_SPAWN_ALTITUDE_MSL

        # Set a minimum AGL value for 'alt' if needed,
        # otherwise planes might crash in trees and stuff.
        if alt_type == "RADIO" and alt < MINIMUM_MID_MISSION_SPAWN_ALTITUDE_AGL:
            alt = MINIMUM_MID_MISSION_SPAWN_ALTITUDE_AGL

        group = self.mission.flight_group(
            country=self.country,
            name=name,
            aircraft_type=self.flight.unit_type.dcs_unit_type,
            airport=None,
            position=pos,
            altitude=alt.meters,
            speed=speed.kph,
            maintask=None,
            group_size=self.flight.count,
        )

        group.points[0].alt_type = alt_type
        return group

    def _generate_at_airfield(self, name: str, airfield: Airfield) -> FlyingGroup[Any]:
        # TODO: Delayed runway starts should be converted to air starts for multiplayer.
        # Runway starts do not work with late activated aircraft in multiplayer. Instead
        # of spawning on the runway the aircraft will spawn on the taxiway, potentially
        # somewhere that they don't fit anyway. We should either upgrade these to air
        # starts or (less likely) downgrade to warm starts to avoid the issue when the
        # player is generating the mission for multiplayer (which would need a new
        # option).
        try:
            self.flight.unit_type.dcs_unit_type.load_payloads()
        except KeyError:
            print(
                "Error loading loadout for mission "
                + self.flight.flight_type.__str__()
                + ", aircraft "
                + self.flight.unit_type.dcs_unit_type.id
            )
            print("Retrying...")
            self.flight.unit_type.dcs_unit_type.load_payloads()
        return self.mission.flight_group_from_airport(
            country=self.country,
            name=name,
            aircraft_type=self.flight.unit_type.dcs_unit_type,
            airport=airfield.airport,
            maintask=None,
            start_type=self._start_type_at_airfield(airfield),
            group_size=self.flight.count,
            parking_slots=None,
        )

    def _generate_over_departure(
        self, name: str, origin: ControlPoint
    ) -> FlyingGroup[Any]:
        at = origin.position

        alt_type = "RADIO"
        if isinstance(origin, OffMapSpawn):
            alt = self.flight.flight_plan.waypoints[0].alt
            alt_type = self.flight.flight_plan.waypoints[0].alt_type
        elif self.flight.unit_type.helicopter:
            alt = WARM_START_HELI_ALT
        else:
            alt = WARM_START_ALTITUDE

        speed = GroundSpeed.for_flight(self.flight, alt)
        pos = at + Vector2(random.randint(100, 1000), random.randint(100, 1000))

        group = self.mission.flight_group(
            country=self.country,
            name=name,
            aircraft_type=self.flight.unit_type.dcs_unit_type,
            airport=None,
            position=pos,
            altitude=alt.meters,
            speed=speed.kph,
            maintask=None,
            group_size=self.flight.count,
        )

        group.points[0].alt_type = alt_type
        return group

    def _generate_at_group(
        self, name: str, at: Union[ShipGroup, StaticGroup]
    ) -> FlyingGroup[Any]:
        return self.mission.flight_group_from_unit(
            country=self.country,
            name=name,
            aircraft_type=self.flight.unit_type.dcs_unit_type,
            pad_group=at,
            maintask=None,
            start_type=self._start_type_at_group(at),
            group_size=self.flight.count,
        )

    def _generate_at_cp_helipad(
        self, name: str, cp: ControlPoint
    ) -> Optional[FlyingGroup[Any]]:
        try:
            helipad = self.helipads[cp].pop()
        except IndexError as ex:
            logging.warning("Not enough helipads available at " + str(ex))
            if isinstance(cp, Airfield):
                return self._generate_at_airfield(name, cp)
            else:
                return None
            # raise RuntimeError(f"Not enough helipads available at {cp}") from ex

        group = self._generate_at_group(name, helipad)

        # Note : A bit dirty, need better support in pydcs
        group.points[0].action = PointAction.FromGroundArea
        group.points[0].type = "TakeOffGround"
        group.units[0].heading = helipad.units[0].heading
        if self.start_type is not StartType.COLD:
            group.points[0].action = PointAction.FromGroundAreaHot
            group.points[0].type = "TakeOffGroundHot"

        for i in range(self.flight.count - 1):
            try:
                helipad = self.helipads[cp].pop()
                terrain = cp.coalition.game.theater.terrain
                group.units[1 + i].position = Point(
                    helipad.x, helipad.y, terrain=terrain
                )
                group.units[1 + i].heading = helipad.units[0].heading
            except IndexError as ex:
                logging.warning("Not enough helipads available at " + str(ex))
                if isinstance(cp, Airfield):
                    return self._generate_at_airfield(name, cp)
                else:
                    return None
        return group

    def _generate_at_cp_stol(
        self, name: str, cp: ControlPoint
    ) -> Optional[FlyingGroup[Any]]:
        try:
            if len(self.stol_pads_roadbase[cp]) > 0:
                stol_pad = self.stol_pads_roadbase[cp].pop()
            else:
                stol_pad = self.stol_pads[cp].pop()
        except IndexError as ex:
            logging.warning("Not enough STOL slots available at " + str(ex))
            return None
            # raise RuntimeError(f"Not enough STOL slots available at {cp}") from ex

        group = self._generate_at_group(name, stol_pad[0])

        # Note : A bit dirty, need better support in pydcs
        group.points[0].action = PointAction.FromGroundArea
        group.points[0].type = "TakeOffGround"
        group.units[0].heading = stol_pad[0].units[0].heading

        # Evaluate hot starts
        # The Mirage 2000C currently has a bug (as of DCS World 2.8.0.33006) with hot starts from ground
        # which makes takeoffs impossible (gear sticking to the ground), so always cold start them
        if (
            self.start_type is not StartType.COLD
            and self.flight.unit_type.dcs_unit_type not in [M_2000C]
        ):
            group.points[0].action = PointAction.FromGroundAreaHot
            group.points[0].type = "TakeOffGroundHot"

        try:
            cp.coalition.game.scenery_clear_zones
        except AttributeError:
            cp.coalition.game.scenery_clear_zones = []
        cp.coalition.game.scenery_clear_zones.append(stol_pad[1])

        for i in range(self.flight.count - 1):
            try:
                terrain = cp.coalition.game.theater.terrain
                if len(self.stol_pads_roadbase[cp]) > 0:
                    stol_pad = self.stol_pads_roadbase[cp].pop()
                else:
                    stol_pad = self.stol_pads[cp].pop()
                group.units[1 + i].position = Point(
                    stol_pad[0].x, stol_pad[0].y, terrain=terrain
                )
                group.units[1 + i].heading = stol_pad[0].units[0].heading
            except IndexError as ex:
                raise RuntimeError(f"Not enough STOL slots available at {cp}") from ex
        return group

    def dcs_start_type(self) -> DcsStartType:
        # The Mirage 2000C currently has a bug (as of DCS World 2.8.0.33006) with hot starts
        # which makes takeoffs impossible (gear sticking to the ground), so always cold start them
        if self.flight.unit_type.dcs_unit_type in [M_2000C]:
            return DcsStartType.Cold
        elif self.start_type is StartType.RUNWAY:
            return DcsStartType.Runway
        elif self.start_type is StartType.COLD:
            return DcsStartType.Cold
        elif self.start_type is StartType.WARM:
            return DcsStartType.Warm
        raise ValueError(f"There is no pydcs StartType matching {self.start_type}")

    def _start_type_at_airfield(
        self,
        airfield: Airfield,
    ) -> DcsStartType:
        return self.dcs_start_type()

    def _start_type_at_group(
        self,
        at: Union[ShipGroup, StaticGroup],
    ) -> DcsStartType:
        group_units = at.units
        # Setting Su-33s starting from the non-supercarrier Kuznetsov to take off from
        # runway to work around a DCS AI issue preventing Su-33s from taking off when
        # set to "Takeoff from ramp" (#1352)
        # Also setting the F-14A AI variant to start from cats since they are reported
        # to have severe pathfinding problems when doing ramp starts (#1927)
        if self.flight.unit_type.dcs_unit_type == F_14A or (
            self.flight.unit_type.dcs_unit_type == Su_33
            or self.flight.unit_type.dcs_unit_type == AV8BNA
            and group_units[0] is not None
            and group_units[0].type == KUZNECOW.id
        ):
            return DcsStartType.Runway
        else:
            return self.dcs_start_type()
