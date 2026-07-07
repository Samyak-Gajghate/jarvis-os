import pytest

from backend.agents.tools.browser.tool import BrowserTool

@pytest.mark.asyncio
async def test_browser_search():
    tool = BrowserTool()

    results = await tool.search(
        "Jarvis OS"
    )

    assert len(results) > 0
    assert results[0].title