import pytest

from python_design_patterns.design_patterns.creational.builder import PizzaBuilder, PizzaDirector

def test_pizza_builder():
    builder = PizzaBuilder()
    pizza = (
        builder.with_size("Large")
        .with_crust("Thin")
        .with_topping("Pepperoni")
        .with_topping("Cheese")
        .build()
    )
    assert pizza.size == "Large"
    assert pizza.crust == "Thin"
    assert "Pepperoni" in pizza.toppings
    assert "Cheese" in pizza.toppings

def test_pizza_director():
    builder = PizzaBuilder()
    pepperoni_pizza = PizzaDirector.make_pepperoni_pizza(builder)
    assert pepperoni_pizza.size == "Large"
    assert pepperoni_pizza.crust == "Thin"
    assert "Pepperoni" in pepperoni_pizza.toppings

    veggie_pizza = PizzaDirector.make_veggie_pizza(builder)
    assert veggie_pizza.size == "Medium"
    assert veggie_pizza.crust == "Thick"
    assert "Mushrooms" in veggie_pizza.toppings
