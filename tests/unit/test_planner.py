import pytest

from backend.planner.planner import Planner


@pytest.mark.asyncio
async def test_create_plan():
    planner = Planner()

    plan = await planner.create_plan(
        "Write a research paper"
    )

    assert plan.goal == "Write a research paper"
    assert len(plan.tasks) >= 1