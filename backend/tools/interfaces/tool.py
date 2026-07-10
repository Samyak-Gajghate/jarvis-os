from abc import ABC, abstractmethod

from backend.tools.schemas.request import ToolRequest
from backend.tools.schemas.response import ToolResponse


class Tool(ABC):
    """Base interface implemented by every tool."""

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    async def execute(
        self,
        request: ToolRequest,
    ) -> ToolResponse:
        ...