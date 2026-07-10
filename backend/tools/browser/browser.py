from backend.tools.browser.client import BrowserClient
from backend.tools.browser.collector import ContentCollector
from backend.tools.browser.models import PageContent
from backend.tools.browser.ranking import ResultRanker
from backend.tools.browser.schemas import (
    SearchRequest,
    SearchResponse,
)
from backend.tools.browser.search import SearchEngine


class Browser:
    """High-level browser service."""

    def __init__(self):
        self.client = BrowserClient()
        self.search_engine = SearchEngine()
        self.ranker = ResultRanker()
        self.collector = ContentCollector(browser=self)

    async def open(
        self,
        url: str,
    ) -> PageContent:
        return await self.client.open_page(url)

    async def search(
        self,
        query: str,
        max_results: int = 5,
    ) -> SearchResponse:
        response = await self.search_engine.search(
            SearchRequest(
                query=query,
                max_results=max_results,
            )
        )

        response.results = self.ranker.rank(response.results)

        return response