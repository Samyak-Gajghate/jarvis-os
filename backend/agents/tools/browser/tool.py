from backend.agents.tools.browser.client import BrowserClient
from backend.agents.tools.browser.schemas import SearchRequest

class BrowserTool:
    def __init__(self):
        self.client = BrowserClient()

    @property
    def name(self) -> str:
        return "browser"

    async def search(self, query: str):
        return await self.client.search(
            SearchRequest(query=query)
        )