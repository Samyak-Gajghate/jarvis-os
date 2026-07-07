from backend.container.container import Container
from backend.container.providers import register_core_services

container = Container()

register_core_services(container)