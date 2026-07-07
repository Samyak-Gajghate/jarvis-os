from backend.config.manager import ConfigManager
from backend.core.context import ApplicationContext


class Application:
    """Represents the global application."""

    def __init__(self):
        self.config = ConfigManager()
        self.context = ApplicationContext(
            settings=self.config.settings,
        )