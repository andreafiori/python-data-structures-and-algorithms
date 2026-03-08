class Arrays:
    ## Reveerse an array using reverse() method
    def reverse_array(self, arr: list) -> list:
        arr.reverse()
        return arr

    # Reverse an array using a loop    
    def reverse_array_loop(self, arr: list) -> list:
        reversed_arr = []
        for i in range(len(arr)-1, -1, -1):
            reversed_arr.append(arr[i])
        return reversed_arr

    # Rotate array to the right by k steps
    def rotate_array(self, arr: list, k: int) -> list:
        list_of_tuples = zip(*arr[::-1])
        return [list(elem) for elem in list_of_tuples]

    def ruota_orario(self, matrix):
        ruota=list(zip(*reversed(matrix)))
        return[list(elemento) for elemento in ruota]
    
    def ruota_antiorario(self,matrix):
        ruota=list(zip(*reversed(matrix)))
        return[list(elemento)[::-1] for elemento in ruota][::-1]
