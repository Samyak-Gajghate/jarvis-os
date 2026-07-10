from typing import Any

from pydantic import BaseModel, Field


class ToolRequest(BaseModel):
    tool: str
    action: str
    parameters: dict[str, Any] = Field(default_factory=dict)