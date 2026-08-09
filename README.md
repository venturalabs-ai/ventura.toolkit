# ventura.toolkit

![Status](https://img.shields.io/badge/status-shared%20agent%20SDK-blueviolet)
![License](https://img.shields.io/github/license/venturalabs-ai/ventura.toolkit)

**SDK compartilhado de contratos estruturados para agentes, validadores e orquestração do ecossistema Ventura Labs AI.**

## Papel na arquitetura

`ventura.toolkit` padroniza a troca de dados entre Task Classifier, Context Compiler, Model Router, Agent Executor, Ventura.SEG, ferramentas e Validator/Critic.

O objetivo é reduzir texto livre entre agentes e privilegiar contratos estruturados, falha explícita e contexto compacto.

## Contratos implementados

- `AgentTask` — identidade, tipo, objetivo, risco, budget, repositório, referências de contexto e constraints;
- `ValidationReport` — status, checks, erros e warnings, impedindo `passed` com check falho;
- `ExecutionResult` — resultado, artefatos, métricas e validação;
- `compact_refs` — deduplicação e hard cap de referências de contexto.

## Exemplo

```python
from ventura_toolkit.contracts import AgentTask, compact_refs

refs = compact_refs(["src/router.py", "tests/test_router.py", "src/router.py"])
task = AgentTask(
    task_id="fix-router-001",
    task_type="github_change",
    objective="corrigir roteamento sem exceder budget",
    repository="venturalabs-ai/ventura.system",
    risk="normal",
    budget_profile="normal",
    context_refs=refs,
)
```

## Princípios

1. ferramenta determinística antes de LLM;
2. contexto referenciado em vez de dump do repositório;
3. contratos estruturados entre agentes;
4. budgets e risco explícitos;
5. validação não pode ser marcada como sucesso quando checks falham;
6. operações de alto impacto continuam sujeitas aos hard gates de segurança.

## Testar

```bash
python -m unittest discover -s tests -p 'test_toolkit.py' -v
```

O CI também executa compile, testes do SDK, Repository Health, Ventura Autonomy Gate e o baseline compartilhado de segurança.

## Integração

- `ventura.system` — usa os contratos no control plane multimodelo;
- `ventura-agents-2` — descreve agentes/evals que consomem os contratos;
- `Ventura.SEG` — aplica permissões, DLP, secrets e sandbox;
- `ventura.build` — valida perfis, CI e políticas de autonomia.

## Licença

Consulte [LICENSE](LICENSE).
