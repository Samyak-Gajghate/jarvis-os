from fastapi import APIRouter

from backend.container.dependencies import container
from backend.tools.schemas.request import ToolRequest

router = APIRouter()


@router.post("/execute")
async def execute(request: ToolRequest):
    runtime = container.resolve(
        "tool_runtime"
    )

    return await runtime.execute(request)