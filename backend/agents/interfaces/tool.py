from abc import ABC, abstractmethod


class Tool(ABC):
    """Base interface for all tools."""

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    async def execute(self, *args, **kwargs):
        ...