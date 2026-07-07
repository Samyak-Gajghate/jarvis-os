from backend.agents.interfaces.agent import Agent
from backend.agents.schemas.request import AgentRequest
from backend.agents.schemas.response import AgentResponse


class GeneralAgent(Agent):
    """Fallback agent used for general-purpose tasks."""

    @property
    def name(self) -> str:
        return "general"

    async def execute(
        self,
        request: AgentRequest,
    ) -> AgentResponse:

        from backend.container.dependencies import container
        ai = container.resolve("ai_runtime")

        response = await ai.generate(
            user_input=request.description,
            session_id=f"task-{request.task_id}",
        )

        return AgentResponse(
            task_id=request.task_id,
            agent=self.name,
            success=True,
            result=response.text,
        )