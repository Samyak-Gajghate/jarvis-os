from fastapi import APIRouter
from pydantic import BaseModel

from backend.container.dependencies import container


class BrowserRequest(BaseModel):
    url: str


router = APIRouter()


@router.post("/open")
async def open_page(request: BrowserRequest):

    browser = container.resolve("browser_tool")

    return await browser.open(request.url)