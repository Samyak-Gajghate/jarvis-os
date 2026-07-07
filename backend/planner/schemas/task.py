from pydantic import BaseModel, Field


class PlannedTask(BaseModel):
    id: int = Field(..., ge=1)
    title: str
    description: str
    priority: int = Field(default=3, ge=1, le=5)
    depends_on: list[int] = Field(default_factory=list)
    agent: str = "general"
    tool: str | None = None