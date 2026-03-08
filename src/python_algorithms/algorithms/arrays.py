class Arrays:
    def reverse_array(self, arr: list) -> list:
        return arr.reverse()
    
    def reverse_array_loop(self, arr: list) -> list:
        reversed_arr = []
        for i in range(len(arr)-1, -1, -1):
            reversed_arr.append(arr[i])
        return reversed_arr
