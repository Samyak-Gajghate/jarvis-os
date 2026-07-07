from abc import ABC, abstractmethod


class PromptTemplate(ABC):
    """Base class for all prompt templates."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique template name."""
        ...

    @abstractmethod
    def render(self, **kwargs) -> str:
        """Render the prompt using the provided variables."""
        ...