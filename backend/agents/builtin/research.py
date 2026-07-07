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

        # Import locally inside the method to avoid circular imports
        from backend.container.dependencies import container

        browser = container.resolve("browser_tool")
        ai = container.resolve("ai_runtime")

        search_results = await browser.search(
            request.description
        )

        context = "\n".join(
            f"{r.title}\n{r.snippet}"
            for r in search_results
        )

        response = await ai.generate(
            user_input=(
                f"Research the following topic using the "
                f"available search results.\n\n"
                f"Topic:\n{request.description}\n\n"
                f"Results:\n{context}"
            ),
            session_id=f"research-{request.task_id}",
        )

        return AgentResponse(
            task_id=request.task_id,
            agent=self.name,
            success=True,
            result=response.text,
        )
