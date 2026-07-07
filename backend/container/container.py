from typing import Any


class Container:
    """Simple dependency injection container."""

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        self._services[name] = service

    def resolve(self, name: str) -> Any:
        if name not in self._services:
            raise KeyError(f"Service '{name}' is not registered.")
        return self._services[name]

    def has(self, name: str) -> bool:
        return name in self._services