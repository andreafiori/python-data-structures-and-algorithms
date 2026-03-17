import copy

from abc import ABC, abstractmethod

"""
Prototype Design Pattern | https://wikipedia.org/wiki/Prototype_pattern

The Prototype pattern is used to create new objects by copying an existing object (the prototype),
rather than creating new instances from scratch. This is especially useful when object creation is expensive or requires
complex initialization.

Key Takeaways
    The Prototype pattern avoids expensive object creation by cloning.
    copy.deepcopy ensures a deep clone, so changes to the clone do not affect the original.
    Unit tests verify both shallow and deep copy behavior.

"""

"""
Prototype Design Pattern Implementation | https://refactoring.guru/design-patterns/prototype
"""
class Prototype(ABC):
    """Abstract Prototype class that defines the clone method."""

    @abstractmethod
    def clone(self):
        pass

"""
Concrete Prototype class that implements the clone method.
"""
class Document(Prototype):
    """ A concrete prototype that represents a document with a title, content, and metadata. """

    def __init__(self, title: str, content: str, metadata: dict) -> None:
        self.title = title
        self.content = content
        self.metadata = metadata

    def clone(self) -> str:
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f"Document(title='{self.title}', content='{self.content}', metadata={self.metadata})"
