import pytest

from backend.tools.browser.tool import BrowserTool


@pytest.mark.asyncio
async def test_search():

    browser = BrowserTool()

    response = await browser.search(
        "Jarvis operating system",
        3,
    )

    assert len(response.results) > 0