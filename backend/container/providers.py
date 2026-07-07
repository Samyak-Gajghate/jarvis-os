from backend.container.container import Container
from backend.runtime.runtime import Runtime
from backend.runtime.model_manager.manager import ModelManager
from backend.runtime.model_manager.providers.mock import MockProvider


def register_core_services(container: Container) -> None:
    """Register all core services."""
    runtime = Runtime()
    container.register("runtime", runtime)
    # Register ModelManager
    model_manager = ModelManager()
    model_manager.register(MockProvider())
    container.register("model_manager", model_manager)