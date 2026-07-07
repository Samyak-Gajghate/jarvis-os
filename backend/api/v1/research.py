from fastapi import APIRouter
from pydantic import BaseModel

from backend.container.dependencies import container


class ResearchRequest(BaseModel):
    query: str


router = APIRouter()


@router.post("/")
async def research(request: ResearchRequest):
    browser = container.resolve("browser_tool")
    return await browser.search(request.query)