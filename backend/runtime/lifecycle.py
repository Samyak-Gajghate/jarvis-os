import logging

from backend.runtime.service_registry import ServiceRegistry

logger = logging.getLogger(__name__)


class LifecycleManager:
    def __init__(self, registry: ServiceRegistry):
        self.registry = registry

    async def startup(self) -> None:
        logger.info("Starting runtime services...")

        for service in self.registry.all():
            logger.info("Starting %s", service.name)
            await service.start()

    async def shutdown(self) -> None:
        logger.info("Stopping runtime services...")

        for service in reversed(self.registry.all()):
            logger.info("Stopping %s", service.name)
            await service.stop()