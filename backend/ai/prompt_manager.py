from pathlib import Path

from backend.ai.schemas.prompt import Prompt

TEMPLATE_DIR = Path(__file__).parent / "templates"


class PromptManager:
    def load_template(self, name: str) -> str:
        path = TEMPLATE_DIR / f"{name}.md"
        return path.read_text(encoding="utf-8")

    def build_prompt(self, template: str, user_input: str) -> Prompt:
        return Prompt(
            system=self.load_template(template),
            user=user_input,
        )