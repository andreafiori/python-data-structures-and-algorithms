"""
Array reverse
"""
class ArrayReverse:
    """Array reverse utils"""

    def reverse_array(self, arr: list) -> list:
        """ Reverse an array using reverse() method """
        arr.reverse()
        return arr

    def reverse_array_loop(self, arr: list) -> list:
        """ Reverse an array using a loop """
        reversed_arr = []
        for i in range(len(arr)-1, -1, -1):
            reversed_arr.append(arr[i])
        return reversed_arr
