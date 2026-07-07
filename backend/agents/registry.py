from backend.agents.exceptions import AgentNotFoundError
from backend.agents.interfaces.agent import Agent


class AgentRegistry:
    """Registry for all available agents."""

    def __init__(self):
        self._agents: dict[str, Agent] = {}

    def register(self, agent: Agent) -> None:
        self._agents[agent.name] = agent

    def get(self, name: str) -> Agent:
        if name not in self._agents:
            raise AgentNotFoundError(name)

        return self._agents[name]

    def all(self) -> list[Agent]:
        return list(self._agents.values())