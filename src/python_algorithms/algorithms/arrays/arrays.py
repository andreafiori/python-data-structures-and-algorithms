"""
Arrays utils
"""
class Arrays:
    """Class representing a person"""

    def reverse_array(self, arr: list) -> list:
        """Reverse an array using reverse() method"""
        arr.reverse()
        return arr

    def reverse_array_loop(self, arr: list) -> list:
        """ Reverse an array using a loop """
        reversed_arr = []
        for i in range(len(arr)-1, -1, -1):
            reversed_arr.append(arr[i])
        return reversed_arr

    def rotate_array(self, arr: list) -> list:
        """ Rotate array to the right by k steps """
        list_of_tuples = zip(*arr[::-1])
        return [list(elem) for elem in list_of_tuples]

    def ruota_orario(self, matrix):
        """ Rotate matrix clockwise """
        ruota=list(zip(*reversed(matrix)))
        return[list(elemento) for elemento in ruota]

    def ruota_antiorario(self,matrix):
        """ Rotate matrix counterclockwise """
        ruota=list(zip(*reversed(matrix)))
        return[list(elemento)[::-1] for elemento in ruota][::-1]
