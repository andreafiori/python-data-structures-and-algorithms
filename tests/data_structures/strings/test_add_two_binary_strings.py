from python_algorithms.data_structures.strings.add_two_binary_strings import AddTwoBinaryStrings

class TestAddTwoBinaryStrings:

    def setup_class(self):
        self.adder = AddTwoBinaryStrings()

    def test_add_two_binary_strings(self):
        assert self.adder.add("11", "1") == "100"
        assert self.adder.add("1010", "1011") == "10101"

    def test_add_binary(self):
        assert self.adder.addBinary("11", "1") == "100"
        assert self.adder.addBinary("1010", "1011") == "10101"
