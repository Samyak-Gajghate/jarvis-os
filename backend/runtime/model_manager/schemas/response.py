from pydantic import BaseModel


class ModelResponse(BaseModel):
    text: str
    provider: str
    model: str