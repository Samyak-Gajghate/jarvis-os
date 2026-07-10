from backend.tools.browser.browser import Browser
from backend.agents.interfaces.tool import Tool


class BrowserTool(Tool):
    """Browser tool exposed to agents."""

    def __init__(self):
        self.browser = Browser()

    @property
    def name(self) -> str:
        return "browser"

    async def execute(self, url: str):
        return await self.open(url)

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