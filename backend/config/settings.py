from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Jarvis OS"
    app_version: str = "0.1.0"

    debug: bool = True

    host: str = "127.0.0.1"
    port: int = 8000

    ollama_host: str = "http://localhost:11434"
    ollama_model: str = "llama3"

    class Config:
        env_file = ".env"


settings = Settings()