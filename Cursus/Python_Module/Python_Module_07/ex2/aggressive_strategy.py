from ex0 import Creature
from ex1 import TransformCapability

from .battle_strategy import BattleStrategy
from .exceptions import InvalidStrategyError


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this "
                "aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
