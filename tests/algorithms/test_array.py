from python_algorithms.algorithms.arrays.arrays import Arrays

class TestArrays:

    def setup_class(self):
        self.arrays = Arrays()

    def test_reverse(self):
        arr = [1, 2, 3, 4, 5]
        reversed = [5, 4, 3, 2, 1]
        assert self.arrays.reverse_array(arr) == reversed

    def test_reverse_array_loop(self):
        arr = [1, 2, 3, 4, 5]
        reversed = [5, 4, 3, 2, 1]
        assert self.arrays.reverse_array_loop(arr) == reversed
    
    def test_rotate_array(self):
        arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotated = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        assert self.arrays.rotate_array(arr, 1) == rotated

    def test_ruota_orario(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ruotata_orario = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        assert self.arrays.ruota_orario(matrix) == ruotata_orario
