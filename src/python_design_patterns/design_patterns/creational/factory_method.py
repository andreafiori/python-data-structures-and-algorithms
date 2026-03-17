"""
Factory Method Design Pattern | https://wikipedia.org/wiki/Factory_method_pattern

The Factory Method pattern defines an interface for creating an object, but lets subclasses alter the type of objects
that will be created. It's useful when you want to delegate instantiation logic to subclasses, or when you need to decouple
client code from concrete classes.

Key Takeaways
    Factory Method lets subclasses decide which class to instantiate.
    Creator defines the factory method, and Concrete Creators override it.
    Unit tests ensure each document type and editor works as expected.

"""
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def save(self):
        pass

class TextDocument(Document):
    def open(self):
        return "Opening text document"

    def save(self):
        return "Saving text document"

class Spreadsheet(Document):
    def open(self):
        return "Opening spreadsheet"

    def save(self):
        return "Saving spreadsheet"

class Presentation(Document):
    def open(self):
        return "Opening presentation"

    def save(self):
        return "Saving presentation"

class Application(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass

    def new_document(self):
        doc = self.create_document()
        print(doc.open())
        return doc

class TextEditor(Application):
    def create_document(self) -> Document:
        return TextDocument()

class SpreadsheetEditor(Application):
    def create_document(self) -> Document:
        return Spreadsheet()

class PresentationEditor(Application):
    def create_document(self) -> Document:
        return Presentation()
