from backend.tools.browser.schemas import SearchResult


class ResultRanker:
    """Placeholder ranking component."""

    def rank(
        self,
        results: list[SearchResult],
    ) -> list[SearchResult]:
        return results