from backend.runtime.model_manager.schemas.request import ModelRequest
from backend.ai.prompt_manager import PromptManager
from backend.ai.schemas.response import AIResponse
from backend.ai.services.conversation import ConversationService



class AIRuntime:
    def __init__(self):
        self.prompts = PromptManager()
        from backend.container.dependencies import container
        self.models = container.resolve("model_manager")
        self.conversations = ConversationService()

    async def generate(
        self,
        user_input: str,
        session_id: str ,
        template: str = "assistant",
    ) -> AIResponse:

        prompt = self.prompts.build_prompt(
            template,
            user_input,
        )


        # Conversation Management
        session = self.conversations.memory.session(session_id)

        session.add_message(
            "user",
            user_input,
        )

        history = self.conversations.history_text(session_id)

        response = await self.models.generate(
            ModelRequest(
                prompt=f"""
                    {prompt.system}

                    Conversation History:

                    {history}

                    Assistant:
                """
            )
        )

        session.add_message(
            "assistant",
            response.text,
        )

        return AIResponse(
            text=response.text,
            model=response.model,
            provider=response.provider,
        )