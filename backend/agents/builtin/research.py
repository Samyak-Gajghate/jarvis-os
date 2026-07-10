from backend.agents.interfaces.agent import Agent
from backend.agents.schemas.request import AgentRequest
from backend.agents.schemas.response import AgentResponse


class ResearchAgent(Agent):

    @property
    def name(self) -> str:
        return "research"

    async def execute(
        self,
        request: AgentRequest,
    ) -> AgentResponse:

        # Keep this import local to avoid circular import errors
        from backend.container.dependencies import container

        browser = container.resolve("browser_tool")
        ai = container.resolve("ai_runtime")

        page = await browser.open(
            "https://example.com"
        )

        prompt = f"""
Topic:
{request.description}

Page Title:
{page.title}

Content:
{page.text}

Summarize the information relevant to the topic.
"""

        response = await ai.generate(
            user_input=prompt,
            session_id=f"research-{request.task_id}",
        )

        return AgentResponse(
            task_id=request.task_id,
            agent=self.name,
            success=True,
            result=response.text,
        )
