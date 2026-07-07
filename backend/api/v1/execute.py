from fastapi import APIRouter
from pydantic import BaseModel

from backend.container.dependencies import container


class ExecuteRequest(BaseModel):
    goal: str


router = APIRouter()


@router.post("/")
async def execute(request: ExecuteRequest):

    planner = container.resolve("planner")
    dispatcher = container.resolve("dispatcher")

    plan = await planner.create_plan(request.goal)

    results = await dispatcher.dispatch(plan)

    return {
        "plan": plan,
        "results": results,
    }