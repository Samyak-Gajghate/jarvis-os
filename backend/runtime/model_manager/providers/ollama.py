import httpx

from backend.config.settings import settings
from backend.runtime.model_manager.provider import ModelProvider
from backend.runtime.model_manager.schemas.request import ModelRequest
from backend.runtime.model_manager.schemas.response import ModelResponse


class OllamaProvider(ModelProvider):

    @property
    def name(self) -> str:
        return "ollama"

    async def initialize(self) -> None:
        pass

    async def shutdown(self) -> None:
        pass

    async def generate(
        self,
        request: ModelRequest,
    ) -> ModelResponse:

        async with httpx.AsyncClient(timeout=120) as client:

            response = await client.post(
                f"{settings.ollama_host}/api/generate",
                json={
                    "model": request.model or settings.ollama_model,
                    "prompt": request.prompt,
                    "stream": False,
                    "options": {
                        "temperature": request.temperature,
                    },
                },
            )

            response.raise_for_status()

            data = response.json()

            return ModelResponse(
                text=data["response"],
                provider="ollama",
                model=request.model,
            )