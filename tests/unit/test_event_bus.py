import pytest

from backend.events.bus import EventBus
from backend.events.event import Event
from backend.events.subscriber import Subscriber


class TestSubscriber(Subscriber):
    def __init__(self):
        self.called = False

    async def handle(self, event: Event):
        self.called = True


@pytest.mark.asyncio
async def test_publish():
    bus = EventBus()

    subscriber = TestSubscriber()

    bus.subscribe("demo", subscriber)

    await bus.publish(Event(name="demo"))

    assert subscriber.called