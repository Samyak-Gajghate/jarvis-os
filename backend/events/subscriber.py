from abc import ABC, abstractmethod

from backend.events.event import Event


class Subscriber(ABC):
    """Base event subscriber."""

    @abstractmethod
    async def handle(self, event: Event) -> None:
        ...