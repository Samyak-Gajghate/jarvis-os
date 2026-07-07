from enum import Enum


class ProviderType(str, Enum):
    MOCK = "mock"
    OLLAMA = "ollama"
    OPENAI = "openai"
    GEMINI = "gemini"
    GROQ = "groq"
    ANTHROPIC = "anthropic"