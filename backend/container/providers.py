from backend.container.container import Container
from backend.runtime.runtime import Runtime


def register_core_services(container: Container) -> None:
    """Register all core services."""

    runtime = Runtime()

    container.register("runtime", runtime)