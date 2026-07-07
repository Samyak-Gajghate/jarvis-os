from pydantic import BaseModel

from backend.planner.schemas.task import PlannedTask


class ExecutionPlan(BaseModel):
    goal: str
    reasoning: str
    tasks: list[PlannedTask]