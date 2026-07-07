from backend.runtime.model_manager.provider import ModelProvider
from backend.runtime.model_manager.schemas.request import ModelRequest
from backend.runtime.model_manager.schemas.response import ModelResponse


class OllamaProvider(ModelProvider):

    @property
    def name(self) -> str:
        return "ollama"

    async def initialize(self):
        pass

    async def shutdown(self):
        pass

    async def generate(
        self,
        request: ModelRequest,
    ) -> ModelResponse:
        raise NotImplementedError(
            "Implemented in Step 22."
        )