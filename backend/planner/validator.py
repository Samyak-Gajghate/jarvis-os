from backend.planner.schemas import ExecutionPlan


class PlanValidator:
    """Basic validation for execution plans."""

    def validate(self, plan: ExecutionPlan) -> None:
        ids = {task.id for task in plan.tasks}

        for task in plan.tasks:
            for dependency in task.depends_on:
                if dependency not in ids:
                    raise ValueError(
                        f"Unknown dependency: {dependency}"
                    )