from python_algorithms.data_structures.arrays.array_merge import ArrayMerge

class TestArrayMerge:

    def setup_class(self):
        self.arrays = ArrayMerge()

    def test_merge_two_arrays(self):
        arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]
        expected = [1, 2, 3, 4, 5, 6]
        assert self.arrays.merge_two_arrays(arr1, arr2) == expected
