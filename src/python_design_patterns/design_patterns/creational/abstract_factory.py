from abc import ABC, abstractmethod

"""
Abstract Factory Pattern | https://wikipedia.org/wiki/Abstract_factory_pattern

Benefits of the Abstract Factory Pattern
Consistency: enforces a consistent way of creating related objects, ensuring that they work together
Flexibility: Swapping between different families of objects is easy by using different concrete factories.
Scalability: Adding new families of objects involves creating new concrete factories and products,
    making the pattern extensible.
Decoupling: Client code remains decoupled from specific classes,
    allowing for easier maintenance and reducing dependencies.
"""

# Abstract Products
class Laptop(ABC):
    @abstractmethod
    def display(self):
        pass

class Smartphone(ABC):
    @abstractmethod
    def display(self):
        pass

# Concrete Products
class DellLaptop(Laptop):
    def display(self):
        return "Dell Laptop"

class SamsungSmartphone(Smartphone):
    def display(self):
        return "Samsung Smartphone"

# Abstract Factory
class DeviceFactory(ABC):
    @abstractmethod
    def create_laptop(self):
        pass

    @abstractmethod
    def create_smartphone(self):
        pass

# Concrete Factories TO TEST
class DellFactory(DeviceFactory):
    def create_laptop(self):
        return DellLaptop()

    def create_smartphone(self):
        return None  # Dell doesn't make smartphones

class SamsungFactory(DeviceFactory):
    def create_laptop(self):
        return None  # Samsung doesn't make laptops

    def create_smartphone(self):
        return SamsungSmartphone()
