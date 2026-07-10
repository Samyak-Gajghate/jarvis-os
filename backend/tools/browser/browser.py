from backend.tools.browser.client import BrowserClient
from backend.tools.browser.models import PageContent


class Browser:
    """
    High-level browser service.

    This class wraps BrowserClient and will later expose
    searching, navigation, screenshots, downloads,
    DOM interaction, and browser sessions.
    """

    def __init__(self) -> None:
        self.client = BrowserClient()

    async def open(
        self,
        url: str,
    ) -> PageContent:
        return await self.client.open_page(url)