from backend.events.event import Event


class Publisher:
    """Publisher interface."""

    async def publish(self, event: Event) -> None:
        raise NotImplementedError