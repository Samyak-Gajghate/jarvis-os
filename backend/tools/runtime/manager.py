from backend.tools.browser.tool import BrowserTool
from backend.tools.runtime.runtime import ToolRuntime


class ToolManager:
    """Registers built-in tools."""

    def __init__(self):
        self.runtime = ToolRuntime()

        self.runtime.register(
            BrowserTool()
        )