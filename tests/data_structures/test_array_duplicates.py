from python_algorithms.data_structures.arrays.array_duplicates import ArrayDuplicates

class TestArrayDuplicates:

    def setup_class(self):
        self.arrays = ArrayDuplicates()

    def test_remove_duplicates_list(self):
        array = [1, 2, 2, 3, 4, 4, 5]
        expected = [1, 2, 3, 4, 5]
        assert sorted(self.arrays.remove_duplicates_list(array)) == sorted(expected)

    def test_brute_force_duplicate_search(self):
        array_with_duplicates = [1, 2, 3, 1]
        array_without_duplicates = [1, 2, 3, 4]
        assert self.arrays.brute_force_duplicate_search(array_with_duplicates) == True
        assert self.arrays.brute_force_duplicate_search(array_without_duplicates) == False

    def test_better_duplicate_search(self):
        array_with_duplicates = [1, 2, 3, 1]
        array_without_duplicates = [1, 2, 3, 4]
        assert self.arrays.better_duplicate_search(array_with_duplicates) == True
        assert self.arrays.better_duplicate_search(array_without_duplicates) == False

    def test_smart_duplicate_search(self):
        array_with_duplicates = [1, 2, 3, 1]
        array_without_duplicates = [1, 2, 3, 4]
        assert self.arrays.smart_duplicate_search(array_with_duplicates) == True
        assert self.arrays.smart_duplicate_search(array_without_duplicates) == False