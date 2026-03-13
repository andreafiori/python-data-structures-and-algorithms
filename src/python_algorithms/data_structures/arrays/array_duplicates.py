"""
Array duplicates
"""
class ArrayDuplicates:
    """Array duplicates utils"""

    def remove_duplicates_list(self, array):
        """ Remove duplicates from array """
        return list(set(array))

    def brute_force_duplicate_search(self, array):
        """
        Given an array of integers, find if the array contains any duplicates.
        Return true if any value appears at least twice in the array,
        and it should return false if every element is distinct.
        Time Complexity - O(n^2)
        """
        for i in range(len(array)-1):
            for j in range(i+1,len(array)):
                if array[i] == array[j]:
                    return True
        return False

    def better_duplicate_search(self, array):
        """
        A slightly better solution can be :
        First we sort the array using O(nlog n) built-in sort of Python.
        Loop through the array once to check if any consecutive elements are same
        So overall complexity will be O(nlog n)
        """
        array.sort()
        for i in range(len(array)-1):
            if array[i] == array[i+1]:
                return True
        return False

    def smart_duplicate_search(self, array):
        """
        An even better solution can be using a dictionary.
        Loop through the array, check first if the current element is present in the dictionary
        If yes, we return True
        If no, we add the element to the dictionary.
        Since looking up in a dictionary is O(1) time, overall complexity would be O(n)
        """
        dictionary = {}
        if len(array) < 2:
            return False

        for _, el in enumerate(array):
            if el in dictionary:
                return True
            dictionary[el] = True

        return False
