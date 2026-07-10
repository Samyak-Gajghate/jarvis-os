from backend.tools.browser.models import PageContent
from backend.tools.browser.schemas import SearchResult


class ContentCollector:
    """Collect content from multiple pages."""

    def __init__(self, browser=None):
        self._browser = browser

    @property
    def browser(self):
        if self._browser is None:
            from backend.tools.browser.browser import Browser
            self._browser = Browser()
        return self._browser

    async def collect(
        self,
        results: list[SearchResult],
    ) -> list[PageContent]:

        pages: list[PageContent] = []

        for result in results:
            try:
                page = await self.browser.open(result.url)
                pages.append(page)
            except Exception:
                continue

        return pages