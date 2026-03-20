from python_algorithms.data_structures.strings.first_non_repeating import FirstNonRepeating

class TestFirstNonRepeating:

    def setup_class(self):
        self.first_non_repeating = FirstNonRepeating()

    def test_first_non_repeating(self):
        assert self.first_non_repeating.find_non_repeating1("leetcode") == "l"
        assert self.first_non_repeating.find_non_repeating1("loveleetcode") == "v"
        assert self.first_non_repeating.find_non_repeating1("aabb") == -1
