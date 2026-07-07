from backend.agents.manager import AgentManager
from backend.agents.schemas.response import AgentResponse
from backend.planner.schemas import ExecutionPlan


class TaskDispatcher:
    """Dispatches tasks from an execution plan."""

    def __init__(self):
        self.manager = AgentManager()

    async def dispatch(
        self,
        plan: ExecutionPlan,
    ) -> list[AgentResponse]:

        results: list[AgentResponse] = []

        for task in plan.tasks:
            result = await self.manager.execute(task)
            results.append(result)

        return results