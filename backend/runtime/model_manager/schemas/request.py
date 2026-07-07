from pydantic import BaseModel


class ModelRequest(BaseModel):
    prompt: str
    model: str = "llama3"
    temperature: float = 0.7
    max_tokens: int = 1024