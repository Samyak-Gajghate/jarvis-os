class ToolRuntimeError(Exception):
    """Base tool runtime exception."""


class ToolNotFoundError(ToolRuntimeError):
    """Raised when a requested tool is unavailable."""


class ToolExecutionError(ToolRuntimeError):
    """Raised when a tool fails during execution."""