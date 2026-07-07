from backend.runtime.model_manager.provider import ModelProvider
from backend.runtime.model_manager.registry import ProviderRegistry
from backend.runtime.model_manager.schemas.request import ModelRequest
from backend.runtime.model_manager.schemas.response import ModelResponse


class ModelManager:
    """Central AI model manager."""

    def __init__(self):
        self.registry = ProviderRegistry()
        self.default_provider = "mock"

    def register(self, provider: ModelProvider):
        self.registry.register(provider)

    async def initialize(self):
        for provider in self.registry.all():
            await provider.initialize()

    async def shutdown(self):
        for provider in self.registry.all():
            await provider.shutdown()

    async def generate(
        self,
        request: ModelRequest,
    ) -> ModelResponse:
        provider = self.registry.get(self.default_provider)

        return await provider.generate(request)