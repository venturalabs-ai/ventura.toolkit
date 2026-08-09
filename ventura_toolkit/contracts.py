from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence


_ALLOWED_RISK = {"low", "normal", "high"}
_ALLOWED_BUDGET = {"simple", "normal", "critical"}
_ALLOWED_STATUS = {"passed", "failed", "blocked"}


@dataclass(frozen=True)
class AgentTask:
    task_id: str
    task_type: str
    objective: str
    repository: str | None = None
    risk: str = "normal"
    budget_profile: str = "normal"
    context_refs: tuple[str, ...] = ()
    constraints: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.task_id.strip():
            raise ValueError("task_id is required")
        if not self.task_type.strip():
            raise ValueError("task_type is required")
        if not self.objective.strip():
            raise ValueError("objective is required")
        if self.risk not in _ALLOWED_RISK:
            raise ValueError(f"risk must be one of {sorted(_ALLOWED_RISK)}")
        if self.budget_profile not in _ALLOWED_BUDGET:
            raise ValueError(f"budget_profile must be one of {sorted(_ALLOWED_BUDGET)}")

    def to_payload(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "task_type": self.task_type,
            "objective": self.objective,
            "repository": self.repository,
            "risk": self.risk,
            "budget_profile": self.budget_profile,
            "context_refs": list(self.context_refs),
            "constraints": dict(self.constraints),
        }


@dataclass(frozen=True)
class ValidationReport:
    status: str
    checks: Mapping[str, bool]
    errors: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.status not in _ALLOWED_STATUS:
            raise ValueError(f"status must be one of {sorted(_ALLOWED_STATUS)}")
        if self.status == "passed" and (self.errors or not all(self.checks.values())):
            raise ValueError("passed validation cannot contain failed checks or errors")

    @property
    def passed(self) -> bool:
        return self.status == "passed"


@dataclass(frozen=True)
class ExecutionResult:
    task_id: str
    status: str
    summary: str
    artifacts: tuple[str, ...] = ()
    metrics: Mapping[str, float | int | bool] = field(default_factory=dict)
    validation: ValidationReport | None = None

    def __post_init__(self) -> None:
        if self.status not in _ALLOWED_STATUS:
            raise ValueError(f"status must be one of {sorted(_ALLOWED_STATUS)}")
        if self.status == "passed" and self.validation is not None and not self.validation.passed:
            raise ValueError("passed execution requires passed validation when validation is present")

    def artifact_count(self) -> int:
        return len(self.artifacts)


def compact_refs(refs: Sequence[str], max_items: int = 20) -> tuple[str, ...]:
    """Deduplicate context references while preserving order and enforcing a hard cap."""
    if max_items < 1:
        raise ValueError("max_items must be positive")
    seen: set[str] = set()
    compacted: list[str] = []
    for ref in refs:
        value = ref.strip()
        if not value or value in seen:
            continue
        seen.add(value)
        compacted.append(value)
        if len(compacted) >= max_items:
            break
    return tuple(compacted)
