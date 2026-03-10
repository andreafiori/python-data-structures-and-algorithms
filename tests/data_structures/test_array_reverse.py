from python_algorithms.data_structures.arrays.array_reverse import ArrayReverse

class TestArrayReverse:

    def setup_class(self):
        self.array_rev = ArrayReverse()

    def test_reverse(self):
        arr = [1, 2, 3, 4, 5]
        reversed = [5, 4, 3, 2, 1]
        assert self.array_rev.reverse_array(arr) == reversed

    def test_reverse_array_loop(self):
        arr = [1, 2, 3, 4, 5]
        reversed = [5, 4, 3, 2, 1]
        assert self.array_rev.reverse_array_loop(arr) == reversed
