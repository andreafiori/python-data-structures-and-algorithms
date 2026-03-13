"""
Calculator utils
"""
class Calculator:
    """ Class to perform addition without using the + operator. """

    def add_without_operator(self, a, b):
        """ Add two numbers without using the + operator """
        while b != 0:
            # carry now contains common set bits of x and y
            carry = a & b
            # Sum of bits of x and y where at least one of the bits is not set
            a = a ^ b
            # Carry is shifted by one so that adding it to x gives the required sum
            b = carry << 1
        return a

    def multiply_without_operator(self, a, b):
        """ Multiply two numbers without using the * operator """
        result = 0
        while b > 0:
            # If b is odd, add a to result
            if b & 1:
                result = self.add_without_operator(result, a)
            # Double a and halve b
            a <<= 1
            b >>= 1
        return result

    def divide_without_operator(self, a, b):
        """ Divide two numbers without using the / operator """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        quotient = 0
        while a >= b:
            a = self.add_without_operator(a, -b)
            quotient = self.add_without_operator(quotient, 1)
        return quotient

    def power_without_operator(self, a, b):
        """ Calculate a raised to the power of b without using the ** operator """
        result = 1
        while b > 0:
            # If b is odd, multiply result by a
            if b & 1:
                result = self.multiply_without_operator(result, a)
            # Square a and halve b
            a = self.multiply_without_operator(a, a)
            b >>= 1
        return result
