from backend.tools.interfaces.tool import Tool
from backend.tools.runtime.exceptions import ToolNotFoundError


class ToolRegistry:
    """Registry of available tools."""

    def __init__(self):
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool:
        if name not in self._tools:
            raise ToolNotFoundError(name)

        return self._tools[name]

    def all(self) -> list[Tool]:
        return list(self._tools.values())