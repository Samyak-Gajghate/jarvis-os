from pathlib import Path

from backend.ai.runtime import AIRuntime
from backend.planner.parser import PlannerParser
from backend.planner.schemas import Plan

PROMPT = (
    Path(__file__).parent / "prompts" / "planner.md"
).read_text(encoding="utf-8")


class Planner:
    def __init__(self):
        self.ai = AIRuntime()
        self.parser = PlannerParser()

    async def create_plan(self, goal: str) -> Plan:
        response = await self.ai.generate(
            user_input=f"{PROMPT}\n\nGoal:\n{goal}",
            session_id="planner-system",
            template="planner",
        )

        return self.parser.parse(goal, response.text)