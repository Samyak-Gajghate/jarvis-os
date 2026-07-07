from dataclasses import dataclass, field


@dataclass
class ConversationContext:
    history: list[str] = field(default_factory=list)

    def add(self, message: str) -> None:
        self.history.append(message)