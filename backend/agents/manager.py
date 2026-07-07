from backend.agents.builtin.general import GeneralAgent
from backend.agents.interfaces.agent import Agent
from backend.agents.registry import AgentRegistry
from backend.agents.schemas.request import AgentRequest
from backend.agents.schemas.response import AgentResponse
from backend.planner.schemas.task import PlannedTask
from backend.agents.exceptions import AgentNotFoundError
from backend.agents.builtin.research import ResearchAgent


class AgentManager:
    """Coordinates execution using registered agents."""

    def __init__(self):
        self.registry = AgentRegistry()
        self.registry.register(GeneralAgent())
        self.registry.register(ResearchAgent())

    def register(self, agent: Agent) -> None:
        self.registry.register(agent)

    async def execute(
        self,
        task: PlannedTask,
    ) -> AgentResponse:

        try:
            agent = self.registry.get(task.agent)
        except AgentNotFoundError:
            agent = self.registry.get("general")

        request = AgentRequest(
            task_id=task.id,
            title=task.title,
            description=task.description,
        )

        return await agent.execute(request)