# Skill: ventura.toolkit — LOOP Skill Engine / Deterministic Replay

![MIT](https://img.shields.io/github/license/chamseddinehiddoud/ventura.toolkit)
![stars](https://img.shields.io/github/stars/chamseddinehiddoud/ventura.toolkit)
![forks](https://img.shields.io/github/forks/chamseddinehiddoud/ventura.toolkit)

Skill de construção e iteração de interfaces (UI) usando **execução
determinística**: explore a feature uma vez, compile o design em `ui.md`,
replique a implementação do componente com ~zero tokens, regenere quando os
requisitos mudarem.

## Trigger

Use quando o usuário quiser: construir telas/componentes, "qual o próximo
componente", iterar em UI existente, revisar design de componentes, decidir
estado/estrutura de interface.

## Arquitetura Token-Efficient & Regenerative

| Fase | Descrição | Consumo |
|---|---|---|
| **Explore** | Modelo forte analisa requisitos + UI alvo (uma vez) | Alto (único) |
| **Compile** | Gera `ui.md`: componentes, props, estado, contratos, testes | Baixo |
| **Replay** | Implementa o componente do dia — props, estado, teste | Mínimo/Zero |
| **Regenerate** | Requisitos mudaram → regenere o design | Sob demanda |

## Receita determinística (Replay)

```text
1. PEDIDO   — "próximo componente" | "implementar X" | "revisar UI"
2. RECEITA  — consulta ui.md: componente N, props, estado, contrato, teste
3. EXECUTA  — 1. componente com contrato de props
             2. estado mínimo (derive o resto)
             3. teste do comportamento principal
4. REGISTRA — progresso, decisões, dúvidas, data
5. STOP-YIELD — requisito vago → pergunta única antes de implementar
```

## Regras de engenharia

- **Token Budget** — Explore: até 6k tokens. Replay: < 200 tokens.
- **Context Firewall** — o replay só vê o componente do dia (nunca o design inteiro).
- **Prefix Caching** — o sistema deste arquivo fica byte-stable.
- **Skill Distillation** — padrão validado vira parte do toolkit permanente.
- **Regeneração** — nova feature/tela → volta ao Explore com memória.

## Como compilar o design (Explore → Compile)

```text
1. Entrevista rápida: tela/feature, stack, estado atual, requisitos
2. Aplica as camadas do toolkit: componentes, estado, render, composição
3. Compila ui.md: componentes, props, estado, contratos, testes, ordem
4. Valida com o usuário e ativa o Replay
```

## Exemplo de uso

```text
Atue como ventura.toolkit (modo REPLAY). Meu ui.md diz: "Componente 3 —
lista de itens: props itens[], estado selecionado (derivado), teste de
renderização". Implemente com contrato de tipos claro e teste principal.
Use menos de 200 tokens e registre o progresso.
```
