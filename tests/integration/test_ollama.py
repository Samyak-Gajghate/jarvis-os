import pytest

from backend.container.dependencies import container
from backend.runtime.model_manager.schemas.request import ModelRequest


@pytest.mark.asyncio
async def test_ollama_generation():

    manager = container.resolve("model_manager")

    response = await manager.generate(
        ModelRequest(
            prompt="Hello Jarvis"
        )
    )

    assert response.provider == "ollama"
    assert len(response.text) > 0