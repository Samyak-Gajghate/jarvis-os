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
        # Dynamically retrieve registered agent names from the container
        from backend.container.dependencies import container
        dispatcher = container.resolve("dispatcher")
        available_agents = [agent.name for agent in dispatcher.manager.registry.all()]
        agents_list_str = ", ".join(f"'{name}'" for name in available_agents)

        # Inject available agents into the prompt instructions
        prompt_with_agents = f"{PROMPT}\n\nAvailable Agents: [{agents_list_str}]"

        response = await self.ai.generate(
            user_input=f"{prompt_with_agents}\n\nGoal:\n{goal}",
            session_id="planner-system",
            template="planner",
        )

        plan = self.parser.parse(response.text)

        self.validator.validate(plan)

        return plan
