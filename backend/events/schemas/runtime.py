from backend.events.event import Event


class RuntimeStarted(Event):
    def __init__(self):
        super().__init__(name="runtime.started")


class RuntimeStopped(Event):
    def __init__(self):
        super().__init__(name="runtime.stopped")