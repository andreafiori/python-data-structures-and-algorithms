"""
Fibonacci algorithms using different techniques
"""
import math

class Fibonacci:
    """Fibonacci algorithms using different techniques"""

    def fibonacci_recursive(self, n):
        """Recursive implementation (O(2^n) time, O(n) space)"""
        if n == 0:
            return 0
        return 1 if n==1 else self.fibonacci_recursive(n-1) + self.fibonacci_recursive(n-2)

    def fibonacci_iterative(self, n):
        """Iterative implementation (O(n) time, O(1) space)"""
        if n == 0:
            return 0
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

    def fibonacci_dp(self, n, memo=None):
        """Dynamic programming with memoization (O(n) time, O(n) space)"""
        if memo is None:
            memo = {0: 0, 1: 1}
        if n not in memo:
            memo[n] = self.fibonacci_dp(n-1, memo) + self.fibonacci_dp(n-2, memo)
        return memo[n]

    def fibonacci_closed_form(self, n):
        """Closed-form (Binet's formula) (O(1) time, O(1) space)"""
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        return round((phi**n - (-phi)**(-n)) / sqrt5)
