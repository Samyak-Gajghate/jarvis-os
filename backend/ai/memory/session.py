from dataclasses import dataclass, field

from backend.ai.memory.schemas import Message


@dataclass
class ConversationSession:
    session_id: str
    messages: list[Message] = field(default_factory=list)

    def add_message(self, role: str, content: str) -> None:
        self.messages.append(
            Message(role=role, content=content)
        )