# ventura.toolkit

![MIT](https://img.shields.io/github/license/chamseddinehiddoud/ventura.toolkit)
![stars](https://img.shields.io/github/stars/chamseddinehiddoud/ventura.toolkit)
![forks](https://img.shields.io/github/forks/chamseddinehiddoud/ventura.toolkit)

Versão **Ventura** do espírito do *React* — toolkit de pensamento em UI:
componentização, estado, renderização e composição aplicados de forma
pragmática, com uma skill de replay determinístico para construir e iterar
interfaces sem retrabalho.

> **Curadoria original** — este repositório não copia o código-fonte do React;
> ele sintetiza os princípios de design de UI em um kit de trabalho próprio
> (componentização, estado, ciclo de render, composição e performance).

## O que é

Um toolkit de decisão e construção de interfaces: padrões, modelos mentais e
receitas de trabalho organizados em camadas, aplicáveis a qualquer stack
(React, Vue, Svelte, web components ou vanilla).

## Camadas do toolkit

| Camada | Foco | Decisões típicas |
|---|---|---|
| **Componentes** | o que vira componente, props, contratos | granularidade, reuso, naming |
| **Estado** | onde mora o estado, atualização, sincronia | local vs global, derivado |
| **Renderização** | ciclo de render, chaves, reconciliação | listas, idempotência |
| **Composição** | layout de componentes, children, slots | hierarquia, separação |
| **Performance** | memoização, carregamento, bundle | quando otimizar (profile antes) |
| **Acessibilidade** | semântica, teclado, contraste | padrões ARIA, testes |

## Princípios de design

1. **Composição sobre herança** — interfaces crescem por composição.
2. **Estado mínimo** — derive o que puder; só guarde o essencial.
3. **Contratos claros** — props/tipos definem o contrato de cada componente.
4. **Profile antes de otimizar** — medir, depois memoizar.
5. **Acessibilidade é requisito** — não feature.

## Como usar (com a skill)

```text
1. Modo EXPLORE  — defina a tela/feature e os requisitos (uma vez)
2. Modo COMPILE  — registre o design em ui.md: componentes, estado, contratos
3. Modo REPLAY   — implemente o componente do dia: props, estado, teste
4. Modo REGENERATE — requisitos mudaram → regenere o design
```

## Licença

MIT License — Copyright (c) 2026 Wemerson Mota de Oliveira.
