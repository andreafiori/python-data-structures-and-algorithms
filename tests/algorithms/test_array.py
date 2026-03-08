from python_algorithms.algorithms.arrays import Arrays

class TestArrays:

    def test_reverse_array_loop(self):
        arr = [1, 2, 3, 4, 5]
        expected = [5, 4, 3, 2, 1]
        assert Arrays().reverse_array_loop(arr) == expected
