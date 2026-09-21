# sprint_prompt-ia Relatório de Evolução — Sprint 03

## 1. Objetivo

Descrever a evolução do chatbot EV ChargeOps com uso de LangChain, memória por
sessão e guardrails.

## 2. Arquitetura

- Linguagem: Python
- Framework: LangChain
- Modelo: Ollama
- Memória: `RunnableWithMessageHistory` + `InMemoryChatMessageHistory`
- Interface: terminal do VS Code

## 3. Guardrails

Foram definidos controles para:

- impedir prompt injection;
- manter o escopo GoodWe/EV ChargeOps;
- evitar especificações inventadas;
- recusar aconselhamento jurídico, financeiro e instruções de segurança elétrica;
- encaminhar situações de risco para profissional habilitado.

## 4. Comparação de modelos

Preencher após executar o mesmo conjunto de avaliações em pelo menos dois modelos.

| Modelo | Temperature | Top-p | Max tokens | Nota de qualidade | Tokens/turno | Latência média | Segurança |
|---|---:|---:|---:|---:|---:|---:|---|
| Modelo 1 | 0.1 | 0.9 | 256 | PREENCHER | PREENCHER | PREENCHER | PREENCHER |
| Modelo 2 | 0.1 | 0.9 | 256 | PREENCHER | PREENCHER | PREENCHER | PREENCHER |

## 5. Limitações

- O desempenho depende da memória RAM e do modelo escolhido.
- O computador de execução precisa ter o Ollama funcionando.
- As métricas devem ser coletadas em condições semelhantes.
- As informações técnicas devem ser conferidas na documentação oficial GoodWe.

## 6. Conclusão

Preencher depois dos testes reais, sem declarar que um modelo é superior antes
da comparação dos resultados.
