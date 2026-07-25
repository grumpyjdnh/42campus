from abc import ABC, abstractmethod


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._transformed: bool = False

    @property
    def transformed(self) -> bool:
        return self._transformed

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
