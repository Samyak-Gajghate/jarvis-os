class ModelManagerError(Exception):
    """Base exception for model manager."""


class ProviderNotFound(ModelManagerError):
    """Raised when a provider is unavailable."""