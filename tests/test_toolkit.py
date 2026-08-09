import unittest

from ventura_toolkit.contracts import AgentTask, ExecutionResult, ValidationReport, compact_refs


class ToolkitTests(unittest.TestCase):
    def test_agent_task_rejects_invalid_budget(self):
        with self.assertRaises(ValueError):
            AgentTask(task_id="1", task_type="code", objective="fix", budget_profile="unlimited")

    def test_compact_refs_deduplicates_and_caps_context(self):
        refs = compact_refs(["a.py", "a.py", "b.py", "c.py"], max_items=2)
        self.assertEqual(refs, ("a.py", "b.py"))

    def test_passed_validation_cannot_hide_failed_check(self):
        with self.assertRaises(ValueError):
            ValidationReport(status="passed", checks={"tests": False})

    def test_passed_execution_requires_passed_validation(self):
        validation = ValidationReport(status="failed", checks={"tests": False}, errors=("failure",))
        with self.assertRaises(ValueError):
            ExecutionResult(task_id="1", status="passed", summary="invalid", validation=validation)

    def test_structured_task_payload(self):
        task = AgentTask(
            task_id="task-1",
            task_type="github_change",
            objective="update workflow",
            repository="venturalabs-ai/example",
            context_refs=("workflow.yml",),
        )
        payload = task.to_payload()
        self.assertEqual(payload["repository"], "venturalabs-ai/example")
        self.assertEqual(payload["context_refs"], ["workflow.yml"])


if __name__ == "__main__":
    unittest.main()
