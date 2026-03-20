"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
"""
class FirstNonRepeating:
    """ Time complexity: O(n^2) """

    def find_non_repeating1(self, s: str) -> str:
        """ Brute force approach """
        n = len(s)
        for i in range(n):
            found = False
            for j in range(n):
                if i != j and s[i] == s[j]:
                    found = True
                    break
            if not found:
                return s[i]
        return -1
