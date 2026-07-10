class BrowserToolError(Exception):
    """Base browser exception."""


class PageLoadError(BrowserToolError):
    """Raised when a page cannot be opened."""


class BrowserTimeoutError(BrowserToolError):
    """Raised when browser navigation times out."""