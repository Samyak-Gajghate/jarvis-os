class AgentError(Exception):
    """Base exception for all agent-related errors."""


class AgentNotFoundError(AgentError):
    """Raised when a requested agent is not registered."""

    def __init__(self, agent_name: str):
        super().__init__(f"Agent '{agent_name}' is not registered.")


class AgentExecutionError(AgentError):
    """Raised when an agent fails during execution."""

    def __init__(self, agent_name: str, message: str):
        super().__init__(f"Agent '{agent_name}' failed: {message}")