"""Chatbot GoodWe EV ChargeOps — Sprint 03."""

import time
from typing import Any

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_ollama import ChatOllama

from config import (
    MODEL_NAME,
    OLLAMA_BASE_URL,
    TEMPERATURE,
    TOP_P,
    MAX_TOKENS,
)
from memory import get_session_history
from prompts import SYSTEM_PROMPT


def create_model() -> ChatOllama:
    """Cria o modelo local do Ollama."""
    return ChatOllama(
        model=MODEL_NAME,
        base_url=OLLAMA_BASE_URL,
        temperature=TEMPERATURE,
        num_predict=MAX_TOKENS,
        model_kwargs={"top_p": TOP_P},
    )


def create_chain() -> RunnableWithMessageHistory:
    """Monta o prompt e adiciona memória por sessão."""
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )

    model = create_model()
    chain = prompt | model

    chain_with_history = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )

    return chain_with_history


def ask(
    chain: RunnableWithMessageHistory,
    question: str,
    session_id: str = "demo-session",
) -> dict[str, Any]:
    """Envia uma pergunta e retorna resposta e latência."""
    start = time.perf_counter()

    response = chain.invoke(
        {"input": question},
        config={"configurable": {"session_id": session_id}},
    )

    elapsed = time.perf_counter() - start
    answer = response.content if hasattr(response, "content") else str(response)

    usage = getattr(response, "response_metadata", {})
    return {
        "answer": answer,
        "latency_seconds": round(elapsed, 3),
        "metadata": usage,
    }


def run_demo() -> None:
    """Executa uma demonstração interativa."""
    print("=" * 60)
    print("GoodWe EV ChargeOps — Sprint 03")
    print(f"Modelo: {MODEL_NAME}")
    print("Digite 'sair' para encerrar.")
    print("=" * 60)

    try:
        chain = create_chain()
        session_id = "terminal-session"

        while True:
            question = input("\nVocê: ").strip()

            if question.lower() in {"sair", "exit", "quit"}:
                print("Encerrando.")
                break

            if not question:
                continue

            try:
                result = ask(chain, question, session_id)
                print(f"\nAssistente: {result['answer']}")
                print(f"[Latência: {result['latency_seconds']} s]")
            except Exception as error:
                print("\nErro ao consultar o modelo.")
                print("Verifique se o Ollama está aberto e se o modelo foi instalado.")
                print(f"Detalhe técnico: {error}")

    except Exception as error:
        print("Não foi possível iniciar o chatbot.")
        print(f"Detalhe técnico: {error}")


if __name__ == "__main__":
    run_demo()
