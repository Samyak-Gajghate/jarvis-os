from backend.planner.schemas import ExecutionPlan


class PlanFormatter:
    def to_markdown(self, plan: ExecutionPlan) -> str:
        lines = [f"# Goal\n\n{plan.goal}\n"]

        for task in plan.tasks:
            lines.append(
                f"- [{task.id}] {task.title} "
                f"(Priority {task.priority})"
            )

        return "\n".join(lines)