"""
Reverse a string.
"""
class ReverseString:
    """ Reverse a string using different techniques """

    def slicing(self, s: str) -> str:
        """Using slicing"""
        return s[::-1]

    def reverse_for(self, s: str) -> str:
        """
        Traverse on s in backward direction
        and add each character to the list
        """
        res = []
        for i in range(len(s) - 1, -1, -1):
            res.append(s[i])
        # Convert list back to string
        return ''.join(res)

    def reverse_recursive(self, s: str) -> str:
        """ Using recursion """
        if len(s) == 0:
            return s
        return s[-1] + self.reverse_recursive(s[:-1])

    def reverse_join_for_range(self, s: str) -> str:
        """Using a custom method"""
        return ''.join(s[i] for i in range(len(s) - 1, -1, -1))
