from backend.runtime.model_manager.exceptions import ProviderNotFound
from backend.runtime.model_manager.provider import ModelProvider


class ProviderRegistry:
    """Stores registered model providers."""

    def __init__(self):
        self._providers: dict[str, ModelProvider] = {}

    def register(self, provider: ModelProvider) -> None:
        self._providers[provider.name] = provider

    def get(self, name: str) -> ModelProvider:
        if name not in self._providers:
            raise ProviderNotFound(name)

        return self._providers[name]

    def all(self) -> list[ModelProvider]:
        return list(self._providers.values())