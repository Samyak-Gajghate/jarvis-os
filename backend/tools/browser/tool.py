from typing import Any

from backend.tools.browser.browser import Browser
from backend.tools.interfaces.tool import Tool
from backend.tools.schemas.request import ToolRequest
from backend.tools.schemas.response import ToolResponse


class BrowserTool(Tool):
    """Browser tool exposed to agents."""

    def __init__(self):
        self.browser = Browser()

    @property
    def name(self) -> str:
        return "browser"

    async def execute(
        self,
        request: ToolRequest,
    ):
        if request.action == "search":
            return await self.search(
                request.parameters["query"],
                request.parameters.get(
                    "max_results",
                    5,
                ),
            )

        if request.action == "open":
            return await self.open(
                request.parameters["url"]
            )

        raise ValueError(
            f"Unknown browser action: "
            f"{request.action}"
        )

    async def open(self, url: str):
        return await self.browser.open(url)

    async def search(
        self,
        query: str,
        max_results: int = 5,
    ):
        return await self.browser.search(
            query,
            max_results,
        )