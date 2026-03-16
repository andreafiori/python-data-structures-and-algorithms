"""
Given two binary strings s1 and s2, the task is to return their sum.The input strings may contain leading zeros but the output string should not have any leading zeros.

Example:
    Input: s1 = "1101", s2 = "111"
    Output: "10100"
"""
class AddTwoBinaryStrings:
    """This function adds two binary strings and returns the result as a string."""


    def add(self, s1: str, s2: str) -> str:
        """ This function adds two binary strings and returns the result as a string. """

        # Initialize pointers for both strings
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        result = []

        # Loop until both strings are processed or there is a carry
        while i >= 0 or j >= 0 or carry:
            # Get the current bits from both strings
            bit1 = int(s1[i]) if i >= 0 else 0
            bit2 = int(s2[j]) if j >= 0 else 0

            # Calculate the sum of bits and carry
            total = bit1 + bit2 + carry
            result_bit = total % 2  # The resulting bit is the remainder when divided by 2
            carry = total // 2       # The new carry is the quotient when divided by 2

            # Append the resulting bit to the result list
            result.append(str(result_bit))

            # Move to the next bits
            i -= 1
            j -= 1

        # The result is currently reversed, reverse it back and join to form a string
        return ''.join(reversed(result))

    def trimLeadingZeros(self, s):
        # Find the position of the first '1'
        firstOne = s.find('1')
        return s[firstOne:] if firstOne != -1 else "0"

    # This function adds two binary strings and return
    # result as a third string
    def addBinary(self, s1, s2):
        # Trim Leading Zeros
        s1 = self.trimLeadingZeros(s1)
        s2 = self.trimLeadingZeros(s2)

        n = len(s1)
        m = len(s2)

        # Swap the strings if s1 is of smaller length
        if n < m:
            s1, s2 = s2, s1
            n, m = m, n

        j = m - 1
        carry = 0
        result = []

        # Traverse both strings from the end
        for i in range(n - 1, -1, -1):

            # Current bit of s1
            bit1 = int(s1[i])
            bitSum = bit1 + carry

            # If there are remaining bits in s2
            # add them to the bitSum
            if j >= 0:
                # Current bit of s2
                bit2 = int(s2[j])
                bitSum += bit2
                j -= 1

            # Calculate the result bit and update carry
            bit = bitSum % 2
            carry = bitSum // 2

            # Update the current bit in result
            result.append(str(bit))

        # If there's any carry left, prepend it to the result
        if carry > 0:
            result.append('1')

        return ''.join(result[::-1])
