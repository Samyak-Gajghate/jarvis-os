from backend.ai.memory.session import ConversationSession


class SessionStore:
    """In-memory conversation store."""

    def __init__(self):
        self._sessions: dict[str, ConversationSession] = {}

    def get_or_create(
        self,
        session_id: str,
    ) -> ConversationSession:

        if session_id not in self._sessions:
            self._sessions[session_id] = ConversationSession(
                session_id=session_id
            )

        return self._sessions[session_id]