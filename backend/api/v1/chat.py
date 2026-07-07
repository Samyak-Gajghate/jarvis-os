from fastapi import APIRouter
from pydantic import BaseModel

from backend.container.dependencies import container


class ChatRequest(BaseModel):
    message: str


router = APIRouter()


@router.post("/")
async def chat(request: ChatRequest):
    runtime = container.resolve("ai_runtime")
    return await runtime.generate(request.message)