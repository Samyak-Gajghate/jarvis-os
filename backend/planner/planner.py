from backend import planner
from backend.ai.schemas import response
from pathlib import Path

from backend.ai.runtime import AIRuntime
from backend.planner.parser import PlannerParser
from backend.planner.validator import PlanValidator

PROMPT = (
    Path(__file__).parent / "prompts" / "planner.md"
).read_text(encoding="utf-8")


class Planner:
    def __init__(self):
        self.ai = AIRuntime()
        self.parser = PlannerParser()
        self.validator = PlanValidator()

    async def create_plan(self, goal: str):

        response = await self.ai.generate(
            user_input=f"{PROMPT}\n\nGoal:\n{goal}",
            session_id="planner-system",
            template="planner",
        )

        plan = self.parser.parse(response.text)

        self.validator.validate(plan)

        return plan