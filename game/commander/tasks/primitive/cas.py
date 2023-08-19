from __future__ import annotations

from dataclasses import dataclass
from random import randint

from game.commander.tasks.packageplanningtask import PackagePlanningTask
from game.commander.theaterstate import TheaterState
from game.settings import Settings
from game.theater import FrontLine
from game.ato.flighttype import FlightType


@dataclass
class PlanCas(PackagePlanningTask[FrontLine]):
    settings: Settings

    def preconditions_met(self, state: TheaterState) -> bool:
        # Do not bother planning CAS when there are no enemy ground units at the front.
        # An exception is made for turn zero since that's not being truly planned, but
        # just to determine what missions should be planned on turn 1 (when there *will*
        # be ground units) and what aircraft should be ordered.
        enemy_cp = self.target.control_point_friendly_to(
            player=not state.context.coalition.player
        )

        if self.target not in state.vulnerable_front_lines:
            if (
                state.context.coalition.num_of_planned_cas
                >= state.context.coalition.game.settings.desired_num_of_cas_flights
            ):
                # Append the front line to the list of vulnerable ones if
                # the number of CAS flights has been reached
                state.vulnerable_front_lines.append(self.target)
                return False

            # May still plan a CAS mission despite the front line
            # not being considered vulnerable,
            # more enemy ground units means higher chance to do so
            if enemy_cp.deployable_front_line_units > randint(
                0, enemy_cp.frontline_unit_count_limit
            ):
                state.vulnerable_front_lines.append(self.target)
            else:
                return False

        if enemy_cp.deployable_front_line_units == 0 and state.context.turn > 0:
            return False
        return super().preconditions_met(state)

    def apply_effects(self, state: TheaterState) -> None:
        state.vulnerable_front_lines.remove(self.target)

    def propose_flights(self) -> None:
        if self.target.is_friendly(False):
            self.propose_flight(FlightType.CAS, 2)
            self.propose_flight(FlightType.TARCAP, 2)
            self.propose_flight(FlightType.SEAD_ESCORT, 2)
        else:
            self.propose_flight(FlightType.CAS, randint(2, 4))
            self.propose_flight(FlightType.TARCAP, randint(2, 4))
            self.propose_flight(FlightType.SEAD_ESCORT, randint(2, 4))
        if randint(1, 100) <= self.settings.autoplan_tankers_for_cas:
            self.propose_flight(FlightType.REFUELING, 1)
