from abc import ABC, abstractmethod


class Service(ABC):
    """Base interface for every runtime service."""

    @abstractmethod
    async def start(self) -> None:
        ...

    @abstractmethod
    async def stop(self) -> None:
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        ...