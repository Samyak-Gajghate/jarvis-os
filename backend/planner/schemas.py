from pydantic import BaseModel

from backend.planner.models.task import Task


class Plan(BaseModel):
    goal: str
    tasks: list[Task]