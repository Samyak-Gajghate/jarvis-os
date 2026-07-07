class RuntimeError(Exception):
    """Base runtime exception."""


class ServiceAlreadyRegistered(RuntimeError):
    """Raised when a duplicate service is registered."""


class ServiceNotFound(RuntimeError):
    """Raised when a requested service does not exist."""