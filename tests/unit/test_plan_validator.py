from backend.planner.schemas import ExecutionPlan, PlannedTask
from backend.planner.validator import PlanValidator


def test_valid_plan():
    plan = ExecutionPlan(
        goal="Demo",
        reasoning="Test",
        tasks=[
            PlannedTask(
                id=1,
                title="Task",
                description="Demo",
                priority=1,
            )
        ],
    )

    PlanValidator().validate(plan)