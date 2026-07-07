from backend.ai.memory.manager import ConversationMemoryManager


class ConversationService:

    def __init__(self):
        self.memory = ConversationMemoryManager()

    def history_text(self, session_id: str) -> str:

        session = self.memory.session(session_id)

        return "\n".join(
            f"{m.role}: {m.content}"
            for m in session.messages
        )