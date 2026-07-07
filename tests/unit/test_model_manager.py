import pytest

from backend.runtime.model_manager.manager import ModelManager
from backend.runtime.model_manager.providers.mock import MockProvider
from backend.runtime.model_manager.schemas.request import ModelRequest


@pytest.mark.asyncio
async def test_mock_generation():

    manager = ModelManager()

    manager.register(MockProvider())

    response = await manager.generate(
        ModelRequest(prompt="Hello")
    )

    assert response.provider == "mock"
    assert "Hello" in response.text