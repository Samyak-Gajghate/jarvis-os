from backend.container.container import Container
from backend.runtime.runtime import Runtime
from backend.runtime.model_manager.manager import ModelManager
from backend.runtime.model_manager.providers.ollama import OllamaProvider


def register_core_services(container: Container) -> None:
    """Register all core services."""
    runtime = Runtime()
    container.register("runtime", runtime)
    # Register ModelManager
    model_manager = ModelManager()
    provider = OllamaProvider()
    model_manager.register(provider)
    model_manager.default_provider = "ollama"
    container.register("model_manager", model_manager)