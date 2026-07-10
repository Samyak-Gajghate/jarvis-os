from fastapi import APIRouter
from pydantic import BaseModel

from backend.container.dependencies import container


class SearchRequest(BaseModel):
    query: str
    max_results: int = 5


router = APIRouter()


@router.post("/")
async def search(request: SearchRequest):

    browser = container.resolve("browser_tool")

    return await browser.search(
        request.query,
        request.max_results,
    )