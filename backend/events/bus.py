import asyncio
import logging
from collections import defaultdict

from backend.events.event import Event
from backend.events.subscriber import Subscriber

logger = logging.getLogger(__name__)


class EventBus:
    """In-memory asynchronous event bus."""

    def __init__(self) -> None:
        self._subscribers: dict[str, list[Subscriber]] = defaultdict(list)

    def subscribe(self, event_name: str, subscriber: Subscriber) -> None:
        self._subscribers[event_name].append(subscriber)

    async def publish(self, event: Event) -> None:
        logger.info("Publishing event: %s", event.name)

        handlers = self._subscribers.get(event.name, [])

        await asyncio.gather(
            *(subscriber.handle(event) for subscriber in handlers),
            return_exceptions=False,
        )