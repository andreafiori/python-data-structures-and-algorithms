"""
Palindrome algorithms
"""
class Palindrome:
    """Check if a string is a palindrome using various techniques"""

    def is_palindrome_two_pointer(self, s: str) -> bool:
        """Check if a string is a palindrome using the two-pointer technique"""
        is_palindrome = True
        i = 0
        j = 0
        while i < j:
            if s[i] != s[j]:
                is_palindrome = False
                break
            i += 1
            j -= 1

        return is_palindrome

    def is_palindrome_all(self, s: str) -> bool:
        """Check if a string is a palindrome using the all() function"""
        return all(s[i] == s[-i-1] for i in range(len(s)//2))

    def is_palindrome_slicing(self, s: str) -> bool:
        """Check if a string is a palindrome using slicing"""
        return s == s[::-1]

    def is_palindrome_reverse(self, s: str) -> bool:
        """Check if a string is a palindrome using the reversed() function"""
        rev = ''.join(reversed(s))
        return s == rev
