from backend.runtime.interfaces.service import Service
from backend.runtime.exceptions import (
    ServiceAlreadyRegistered,
    ServiceNotFound,
)


class ServiceRegistry:
    """Central registry for runtime services."""

    def __init__(self) -> None:
        self._services: dict[str, Service] = {}

    def register(self, service: Service) -> None:
        if service.name in self._services:
            raise ServiceAlreadyRegistered(service.name)

        self._services[service.name] = service

    def get(self, name: str) -> Service:
        if name not in self._services:
            raise ServiceNotFound(name)

        return self._services[name]

    def all(self) -> list[Service]:
        return list(self._services.values())