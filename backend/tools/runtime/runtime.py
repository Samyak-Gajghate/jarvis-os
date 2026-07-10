from backend.tools.runtime.metrics import ToolMetrics
from backend.tools.runtime.registry import ToolRegistry
from backend.tools.schemas.request import ToolRequest


class ToolRuntime:
    """Universal tool runtime."""

    def __init__(self):
        self.registry = ToolRegistry()
        self.metrics = ToolMetrics()

    def register(self, tool):
        self.registry.register(tool)

    async def execute(self, request: ToolRequest):
        tool = self.registry.get(request.tool)

        try:
            response = await tool.execute(request)
            self.metrics.record_success()
            return response

        except Exception:
            self.metrics.record_failure()
            raise