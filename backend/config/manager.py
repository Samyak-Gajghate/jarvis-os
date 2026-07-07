from backend.config.settings import settings


class ConfigManager:
    """Provides access to application configuration."""

    @property
    def settings(self):
        return settings