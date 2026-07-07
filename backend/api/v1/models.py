from fastapi import APIRouter

from backend.container.dependencies import container
from backend.runtime.model_manager.schemas.request import ModelRequest

router = APIRouter()


@router.post("/generate")
async def generate(request: ModelRequest):

    manager = container.resolve("model_manager")

    return await manager.generate(request)