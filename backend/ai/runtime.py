from backend.runtime.model_manager.schemas.request import ModelRequest
from backend.ai.prompt_manager import PromptManager
from backend.ai.schemas.response import AIResponse


class AIRuntime:
    def __init__(self):
        self.prompts = PromptManager()
        from backend.container.dependencies import container
        self.models = container.resolve("model_manager")

    async def generate(
        self,
        user_input: str,
        template: str = "assistant",
    ) -> AIResponse:

        prompt = self.prompts.build_prompt(
            template,
            user_input,
        )

        response = await self.models.generate(
            ModelRequest(
                prompt=f"{prompt.system}\n\nUser:\n{prompt.user}"
            )
        )

        return AIResponse(
            text=response.text,
            model=response.model,
            provider=response.provider,
        )