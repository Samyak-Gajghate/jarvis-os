import pytest

from backend.tools.browser.tool import BrowserTool


@pytest.mark.asyncio
async def test_browser():

    browser = BrowserTool()

    page = await browser.open(
        "https://example.com"
    )

    assert page.title != ""
    assert len(page.text) > 0