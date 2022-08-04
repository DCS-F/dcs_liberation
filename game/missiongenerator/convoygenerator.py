from __future__ import annotations

import itertools
from typing import TYPE_CHECKING, Optional

from dcs import Mission
from dcs.mapping import Point
from dcs.point import PointAction
from dcs.unit import Vehicle
from dcs.unitgroup import VehicleGroup

from game.dcs.groundunittype import GroundUnitType
from game.missiongenerator.groundforcepainter import GroundForcePainter
from game.theater import FrontLine
from game.transfers import Convoy
from game.unitmap import UnitMap
from game.utils import kph

if TYPE_CHECKING:
    from game import Game


class ConvoyGenerator:
    def __init__(self, mission: Mission, game: Game, unit_map: UnitMap) -> None:
        self.mission = mission
        self.game = game
        self.unit_map = unit_map
        self.count = itertools.count()

    def generate(self) -> None:
        # Reset the count to make generation deterministic.
        for coalition in self.game.coalitions:
            i = 1
            for convoy in coalition.transfers.convoys:
                convoy.name += str(i)
                i += 1
                self.generate_convoy(convoy)

    def generate_convoy(self, convoy: Convoy) -> Optional[VehicleGroup]:
        if self.game.settings.perf_disable_convoys:
            return None
        # Cull the convoy unless the destination is in the culling exclusion zone
        if self.game.position_culled(convoy.route_end):
            return None

        if self.game.settings.convoys_travel_full_distance:
            route_start = convoy.route_start
            route_end = convoy.route_end
        else:
            # convoys_travel_full_distance is disabled, so add the convoy between the route start and route end.
            # This option aims to remove long routes for ground vehicles between control points,
            # since the CPU load for long routes on DCS is pretty heavy.
            frontline = FrontLine(convoy.origin, convoy.destination)

            # Select a segment roughly a third of the way from the origin towards the destination
            # so the convoy spawns between the control points but is still close enough to the
            # origin CP to be targeted by BAI flights and within the protection umbrella of the CP.
            # Convoy start and end waypoints are not the same, so it'll move a little
            # before stopping and hopefully find a road to drive on.
            convoy_segment = int(0.3 * len(frontline.segments))
            route_start = frontline.segments[convoy_segment].point_a
            route_end = frontline.segments[convoy_segment].point_b

        if not convoy.units:
            return None
        group = self._create_mixed_unit_group(
            convoy.name,
            route_start,
            convoy.units,
            convoy.player_owned,
        )

        if self.game.settings.perf_moving_convoys:
            group.add_waypoint(
                route_end,
                speed=kph(40).kph,
                move_formation=PointAction.OnRoad,
            )

        self.make_drivable(group)
        self.unit_map.add_convoy_units(group, convoy)
        return group

    def _create_mixed_unit_group(
        self,
        name: str,
        position: Point,
        units: dict[GroundUnitType, int],
        for_player: bool,
    ) -> VehicleGroup:
        country = self.mission.country(self.game.coalition_for(for_player).country_name)
        faction = self.game.coalition_for(for_player).faction

        unit_types = list(units.items())
        for main_unit_type, main_unit_count in unit_types:
            if main_unit_count > 0:
                break

        group = self.mission.vehicle_group(
            country,
            name,
            main_unit_type.dcs_unit_type,
            position=position,
            group_size=main_unit_count,
            move_formation=PointAction.OnRoad,
        )

        unit_name_counter = itertools.count(main_unit_count + 1)
        # pydcs spreads units out by 20 in the Y axis by default. Pick up where it left
        # off.
        y = itertools.count(position.y + main_unit_count * 20, 20)
        for unit_type, count in unit_types[1:]:
            for i in range(count):
                v = self.mission.vehicle(
                    f"{name} Unit #{next(unit_name_counter)}", unit_type.dcs_unit_type
                )
                v.position.x = position.x
                v.position.y = next(y)
                v.heading = 0
                GroundForcePainter(faction, v).apply_livery()
                group.add_unit(v)

        return group

    @staticmethod
    def make_drivable(group: VehicleGroup) -> None:
        for v in group.units:
            if isinstance(v, Vehicle):
                v.player_can_drive = True
