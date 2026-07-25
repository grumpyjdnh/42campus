from ex0 import Creature
from ex1 import HealCapability
from .battle_strategy import BattleStrategy
from .exceptions import InvalidStrategyError


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())
