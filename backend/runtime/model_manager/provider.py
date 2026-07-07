from abc import ABC, abstractmethod

from backend.runtime.model_manager.schemas.request import ModelRequest
from backend.runtime.model_manager.schemas.response import ModelResponse


class ModelProvider(ABC):
    """Base interface for all AI providers."""

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    async def initialize(self) -> None:
        ...

    @abstractmethod
    async def generate(
        self,
        request: ModelRequest,
    ) -> ModelResponse:
        ...

    @abstractmethod
    async def shutdown(self) -> None:
        ...