import pytest

from backend.agents.dispatcher import TaskDispatcher
from backend.planner.schemas import ExecutionPlan
from backend.planner.schemas.task import PlannedTask


@pytest.mark.asyncio
async def test_dispatch():

    dispatcher = TaskDispatcher()

    plan = ExecutionPlan(
        goal="Demo",
        reasoning="Testing",
        tasks=[
            PlannedTask(
                id=1,
                title="Say Hello",
                description="Respond with Hello",
                priority=1,
                agent="general",
            )
        ],
    )

    results = await dispatcher.dispatch(plan)

    assert len(results) == 1
    assert results[0].success is True
    assert results[0].agent == "general"