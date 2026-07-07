from backend.agents.tools.browser.schemas import SearchRequest, SearchResult

class BrowserClient:
    """
    Placeholder browser client.

    In future steps this will connect to
    Playwright and search providers.
    """

    async def search(
        self,
        request: SearchRequest,
    ) -> list[SearchResult]:

        return [
            SearchResult(
                title="Placeholder Result",
                url="https://example.com",
                snippet=f"Search result for '{request.query}'",
            )
        ]