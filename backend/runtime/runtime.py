import logging

from backend.runtime.lifecycle import LifecycleManager
from backend.runtime.service_registry import ServiceRegistry
from backend.runtime.state import RuntimeState
from backend.events.bus import EventBus
from backend.events.schemas.runtime import (
    RuntimeStarted,
    RuntimeStopped,
)

logger = logging.getLogger(__name__)


class Runtime:
    """Core runtime of Jarvis OS."""

    def __init__(self) -> None:
        self.registry = ServiceRegistry()
        self.lifecycle = LifecycleManager(self.registry)
        self.state = RuntimeState.CREATED
        self.events = EventBus()

    async def start(self) -> None:
        logger.info("Runtime starting")

        self.state = RuntimeState.STARTING

        await self.lifecycle.startup()
        await self.events.publish(RuntimeStarted())
        self.state = RuntimeState.RUNNING

        logger.info("Runtime running")

    async def stop(self) -> None:
        logger.info("Runtime stopping")

        self.state = RuntimeState.STOPPING
        await self.events.publish(RuntimeStopped())
        await self.lifecycle.shutdown()

        self.state = RuntimeState.STOPPED

        logger.info("Runtime stopped")