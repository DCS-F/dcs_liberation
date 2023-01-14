from __future__ import annotations

from dataclasses import dataclass
import random

from game.commander.tasks.packageplanningtask import PackagePlanningTask
from game.commander.theaterstate import TheaterState
from game.theater import FrontLine
from game.ato.flighttype import FlightType


@dataclass
class PlanCas(PackagePlanningTask[FrontLine]):
    def preconditions_met(self, state: TheaterState) -> bool:
        # Do not bother planning CAS when there are no enemy ground units at the front.
        # An exception is made for turn zero since that's not being truly planned, but
        # just to determine what missions should be planned on turn 1 (when there *will*
        # be ground units) and what aircraft should be ordered.
        enemy_cp = self.target.control_point_friendly_to(
            player=not state.context.coalition.player
        )

        if self.target not in state.vulnerable_front_lines:
            # May still plan a CAS mission despite the front line
            # not being considered vulnerable,
            # more enemy ground units means higher chance to do so
            if enemy_cp.deployable_front_line_units > random.randint(
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
        self.propose_flight(FlightType.CAS, 2)
        self.propose_flight(FlightType.TARCAP, 2)
        self.propose_flight(FlightType.SEAD_ESCORT, 2)
        if random.randint(1, 100) > 60:
            self.propose_flight(FlightType.REFUELING, 1)
