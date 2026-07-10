from playwright.async_api import async_playwright

from backend.tools.browser.exceptions import PageLoadError
from backend.tools.browser.extractor import ContentExtractor
from backend.tools.browser.models import PageContent


class BrowserClient:
    """Low-level Playwright client."""

    def __init__(self):
        self.extractor = ContentExtractor()

    async def open_page(
        self,
        url: str,
    ) -> PageContent:

        try:
            async with async_playwright() as p:

                browser = await p.chromium.launch(
                    headless=True
                )

                page = await browser.new_page()

                await page.goto(
                    url,
                    wait_until="networkidle",
                    timeout=60000,
                )

                html = await page.content()

                await browser.close()

            title, text = self.extractor.extract(html)

            return PageContent(
                url=url,
                title=title,
                text=text,
            )

        except Exception as exc:
            raise PageLoadError(str(exc)) from exc