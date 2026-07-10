import pytest

from backend.container.dependencies import container
from backend.tools.schemas.request import ToolRequest


@pytest.mark.asyncio
async def test_browser_search():

    runtime = container.resolve(
        "tool_runtime"
    )

    response = await runtime.execute(
        ToolRequest(
            tool="browser",
            action="search",
            parameters={
                "query": "Jarvis OS",
                "max_results": 2,
            },
        )
    )

    assert response is not None