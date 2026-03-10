"""
Palindrome algorithms
"""
class Palindrome:
    """Check if a string is a palindrome using different techniques"""

    def is_palindrome_all(self, s: str) -> bool:
        """Using the all() function"""
        s = s.lower()
        return all(s[i] == s[-i-1] for i in range(len(s)//2))

    def is_palindrome_slicing(self, s: str) -> bool:
        """Using slicing"""
        s = s.lower()
        return s == s[::-1]

    def is_palindrome_reverse(self, s: str) -> bool:
        """Using the reversed() function"""
        s = s.lower()
        rev = ''.join(reversed(s))
        return s == rev
