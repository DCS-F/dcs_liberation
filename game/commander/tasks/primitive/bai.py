from __future__ import annotations

from dataclasses import dataclass
from random import randint

from game.commander.tasks.packageplanningtask import PackagePlanningTask
from game.commander.theaterstate import TheaterState
from game.theater.theatergroundobject import VehicleGroupGroundObject
from game.ato.flighttype import FlightType


@dataclass
class PlanBai(PackagePlanningTask[VehicleGroupGroundObject]):
    def preconditions_met(self, state: TheaterState) -> bool:
        if not state.has_battle_position(self.target):
            return False
        if not self.target_area_preconditions_met(state):
            return False
        return super().preconditions_met(state)

    def apply_effects(self, state: TheaterState) -> None:
        state.eliminate_battle_position(self.target)

    def propose_flights(self) -> None:
        if not self.target.control_point.coalition.player:
            self.propose_flight(FlightType.BAI, 2)
        else:
            self.propose_flight(FlightType.BAI, randint(2, 4))
        self.propose_common_escorts()
