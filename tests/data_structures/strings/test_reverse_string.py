from python_algorithms.data_structures.strings.reverse_string import ReverseString

class TestPalindrome:

    def setup_class(self):
        self.reverse_string = ReverseString()

    def test_reverse_string_slicing(self):
        s = "hello"
        result = self.reverse_string.slicing(s)
        assert result == "olleh"

    def test_reverse_for(self):
        s = "hello"
        result = self.reverse_string.reverse_for(s)
        assert result == "olleh"

    def test_reverse_recursive(self):
        s = "hello"
        result = self.reverse_string.reverse_recursive(s)
        assert result == "olleh"

    def test_reverse_join_for_range(self):
        s = "hello"
        result = self.reverse_string.reverse_join_for_range(s)
        assert result == "olleh"
