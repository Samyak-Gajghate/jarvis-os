from backend.planner.models.task import Task
from backend.planner.schemas import Plan


class PlannerParser:
    """
    Temporary parser.

    Later this will parse structured JSON produced by the LLM.
    """

    def parse(self, goal: str, response: str) -> Plan:
        return Plan(
            goal=goal,
            tasks=[
                Task(
                    id=1,
                    title="Analyze goal",
                    description=response,
                    priority=1,
                )
            ],
        )