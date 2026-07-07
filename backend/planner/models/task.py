from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int = Field(..., ge=1)
    title: str
    description: str
    priority: int = Field(default=1, ge=1, le=5)
    depends_on: list[int] = Field(default_factory=list)