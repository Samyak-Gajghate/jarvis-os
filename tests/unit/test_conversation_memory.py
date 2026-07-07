from backend.ai.memory.manager import ConversationMemoryManager


def test_session_memory():

    manager = ConversationMemoryManager()

    session = manager.session("abc")

    session.add_message("user", "Hello")

    assert len(session.messages) == 1

    same = manager.session("abc")

    assert len(same.messages) == 1