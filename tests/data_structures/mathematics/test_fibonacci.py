import pytest

from python_algorithms.data_structures.mathematics.fibonacci import Fibonacci

class TestFibonacci:
    """Test suite for the Fibonacci class"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.fib = Fibonacci()

    @pytest.mark.parametrize("n, expected", [
        (0, 0),
        (1, 1),
        (5, 5),
        (10, 55),
    ])
    def test_fibonacci_recursive(self, n, expected):
        assert self.fib.fibonacci_recursive(n) == expected

    @pytest.mark.parametrize("n, expected", [
        (0, 0),
        (1, 1),
        (5, 5),
        (10, 55),
    ])
    def test_fibonacci_iterative(self, n, expected):
        assert self.fib.fibonacci_iterative(n) == expected

    @pytest.mark.parametrize("n, expected", [
        (0, 0),
        (1, 1),
        (5, 5),
        (10, 55),
    ])
    def test_fibonacci_dp(self, n, expected):
        assert self.fib.fibonacci_dp(n) == expected

    @pytest.mark.parametrize("n, expected", [
        (0, 0),
        (1, 1),
        (5, 5),
        (10, 55),
    ])
    def test_fibonacci_closed_form(self, n, expected):
        assert self.fib.fibonacci_closed_form(n) == expected

    @pytest.mark.parametrize("n", range(15))
    def test_all_methods_agree(self, n):
        recursive = self.fib.fibonacci_recursive(n)
        iterative = self.fib.fibonacci_iterative(n)
        dp = self.fib.fibonacci_dp(n)
        closed = self.fib.fibonacci_closed_form(n)
        assert recursive == iterative == dp == closed
