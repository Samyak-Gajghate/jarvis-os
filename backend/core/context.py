from dataclasses import dataclass

from backend.config.settings import Settings


@dataclass
class ApplicationContext:
    settings: Settings