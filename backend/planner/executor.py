from backend.planner.schemas import Plan


class PlanExecutor:
    """
    Placeholder executor.

    In later steps this will dispatch tasks
    to specialized agents.
    """

    async def execute(self, plan: Plan) -> None:
        for task in plan.tasks:
            print(f"Executing: {task.title}")