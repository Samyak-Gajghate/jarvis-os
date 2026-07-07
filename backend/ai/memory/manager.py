from backend.ai.memory.store import SessionStore


class ConversationMemoryManager:

    def __init__(self):
        self.store = SessionStore()

    def session(self, session_id: str):
        return self.store.get_or_create(session_id)