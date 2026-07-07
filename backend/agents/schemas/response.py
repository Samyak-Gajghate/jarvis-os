from pydantic import BaseModel
from typing import Any


class AgentResponse(BaseModel):
    """Standard response returned by every agent."""

    task_id: int
    agent: str
    success: bool
    result: str
    metadata: dict[str, Any] = {}