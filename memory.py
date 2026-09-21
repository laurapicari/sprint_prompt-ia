"""Memória conversacional por sessão."""

from langchain_core.chat_history import InMemoryChatMessageHistory

_store = {}


def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    """Retorna a memória da sessão; cria uma nova se necessário."""
    if session_id not in _store:
        _store[session_id] = InMemoryChatMessageHistory()
    return _store[session_id]


def clear_session(session_id: str) -> None:
    """Apaga a memória de uma sessão."""
    _store.pop(session_id, None)
