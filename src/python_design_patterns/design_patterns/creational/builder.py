"""
Builder Design Pattern | https://wikipedia.org/wiki/Builder_pattern

The Builder pattern is used to construct complex objects step by step,
separating the construction logic from the object itself. This is especially useful when an object requires many parameters
or steps to be created, or when you want to create different representations of the same object.

Use Case
Imagine a pizza ordering system where a pizza can have many optional toppings, sizes, and crust types.
Using a Builder makes it easy to create different pizza configurations without bloating the constructor.

"""
class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []

    def __str__(self):
        return f"Pizza(size={self.size}, crust={self.crust}, toppings={self.toppings})"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def with_size(self, size):
        self.pizza.size = size
        return self

    def with_crust(self, crust):
        self.pizza.crust = crust
        return self

    def with_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def build(self):
        return self.pizza

class PizzaDirector:
    @staticmethod
    def make_pepperoni_pizza(builder):
        return (
            builder.with_size("Large")
            .with_crust("Thin")
            .with_topping("Pepperoni")
            .with_topping("Cheese")
            .build()
        )

    @staticmethod
    def make_veggie_pizza(builder):
        return (
            builder.with_size("Medium")
            .with_crust("Thick")
            .with_topping("Mushrooms")
            .with_topping("Olives")
            .with_topping("Onions")
            .build()
        )
