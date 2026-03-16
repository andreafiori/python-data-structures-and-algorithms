from python_algorithms.data_structures.arrays.array_rotate import ArrayRotate

class TestArrayRotate:

    def setup_class(self):
        self.arrays = ArrayRotate()

    def test_ruota_orario(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ruotata_orario = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        assert self.arrays.ruota_orario(matrix) == ruotata_orario

    def test_ruota_antiorario(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ruotata_antiorario = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
        assert self.arrays.ruota_antiorario(matrix) == ruotata_antiorario