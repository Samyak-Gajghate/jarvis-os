from fastapi import APIRouter
from pydantic import BaseModel

from backend.container.dependencies import container


class PlanRequest(BaseModel):
    goal: str


router = APIRouter()


@router.post("/plan")
async def create_plan(request: PlanRequest):
    planner = container.resolve("planner")
    return await planner.create_plan(request.goal)