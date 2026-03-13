from python_algorithms.data_structures.mathematics.calculator import Calculator

class TestAdditionWithoutOperator:

    def setup_class(self):
        self.calculator = Calculator()

    def test_addition_without_operator(self):
        assert self.calculator.add_without_operator(5, 6) == 11

    def test_multiply_without_operator(self):
        assert self.calculator.multiply_without_operator(5, 6) == 30
