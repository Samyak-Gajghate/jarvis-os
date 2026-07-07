from backend.runtime.model_manager.provider import ModelProvider
from backend.runtime.model_manager.schemas.request import ModelRequest
from backend.runtime.model_manager.schemas.response import ModelResponse


class MockProvider(ModelProvider):

    @property
    def name(self) -> str:
        return "mock"

    async def initialize(self):
        pass

    async def shutdown(self):
        pass

    async def generate(
        self,
        request: ModelRequest,
    ) -> ModelResponse:

        return ModelResponse(
            text=f"Mock response for: {request.prompt}",
            provider="mock",
            model=request.model,
        )