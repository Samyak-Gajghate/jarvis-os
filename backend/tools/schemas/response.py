from typing import Any

from pydantic import BaseModel, Field


class ToolResponse(BaseModel):
    success: bool
    tool: str
    action: str
    result: Any = None
    metadata: dict[str, Any] = Field(default_factory=dict)