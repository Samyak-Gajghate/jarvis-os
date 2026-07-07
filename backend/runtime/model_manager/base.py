from abc import ABC, abstractmethod


class BaseModelProvider(ABC):
    """Abstract interface for all AI model providers."""

    @abstractmethod
    async def load(self) -> None:
        ...

    @abstractmethod
    async def unload(self) -> None:
        ...

    @abstractmethod
    async def generate(self, prompt: str) -> str:
        ...