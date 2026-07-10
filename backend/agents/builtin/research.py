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

        search = await browser.search(
            request.description,
            max_results=3,
        )

        pages = []

        for result in search.results:
            try:
                page = await browser.open(result.url)
                pages.append(page)
            except Exception:
                continue

        context = "\n\n".join(
            f"Title: {page.title}\n\n{page.text[:4000]}"
            for page in pages
        )

        prompt = f"""
Research Topic:

{request.description}

Collected Sources:

{context}

Provide a concise research summary using the collected information.
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