from abc import ABC, abstractmethod

from backend.agents.schemas.request import AgentRequest
from backend.agents.schemas.response import AgentResponse


class Agent(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    async def execute(
        self,
        request: AgentRequest,
    ) -> AgentResponse:
        ...