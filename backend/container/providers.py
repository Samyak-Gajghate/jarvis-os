from backend.container.container import Container
from backend.runtime.runtime import Runtime
from backend.runtime.model_manager.manager import ModelManager
from backend.runtime.model_manager.providers.ollama import OllamaProvider
from backend.ai.runtime import AIRuntime
from backend.planner.planner import Planner
from backend.agents.dispatcher import TaskDispatcher
from backend.agents.tools.browser.tool import BrowserTool


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
    
    #Register AI
    ai_runtime = AIRuntime()
    container.register("ai_runtime", ai_runtime)

    #Register Planner
    planner = Planner()
    container.register("planner", planner)

    #Register Dispatcher
    dispatcher = TaskDispatcher()
    container.register("dispatcher", dispatcher)

    # Register BrowserTool
    browser_tool = BrowserTool()
    container.register("browser_tool", browser_tool)
