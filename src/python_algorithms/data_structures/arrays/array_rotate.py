"""
Array rotate
"""
class ArrayRotate:
    """Array rotate utils"""

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
