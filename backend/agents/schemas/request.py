from pydantic import BaseModel


class AgentRequest(BaseModel):
    task_id: int
    title: str
    description: str