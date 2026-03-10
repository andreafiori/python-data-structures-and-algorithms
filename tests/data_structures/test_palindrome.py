import pytest

from python_algorithms.data_structures.strings.palindrome import Palindrome

class TestPalindrome:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.palindrome = Palindrome()

    @pytest.mark.parametrize("word, expected", [
        ("anna", True),
        ("Anna", True),
        ("python", False),
    ])
    def test_is_palindrome_all(self, word, expected):
        assert self.palindrome.is_palindrome_all(word) == expected

    @pytest.mark.parametrize("word, expected", [
        ("anna", True),
        ("Anna", True),
        ("python", False),
    ])
    def test_is_palindrome_slicing(self, word, expected):
        assert self.palindrome.is_palindrome_slicing(word) == expected

    @pytest.mark.parametrize("word, expected", [
        ("anna", True),
        ("Anna", True),
        ("python", False),
    ])
    def test_is_palindrome_reverse(self, word, expected):
        assert self.palindrome.is_palindrome_reverse(word) == expected

# class TestPalindrome:

#     def setup_class(self):
#         self.palindrome = Palindrome()

#     def test_is_palindrome_all(self):
#         assert self.palindrome.is_palindrome_all("anna") == True
#         assert self.palindrome.is_palindrome_all("Anna") == True

#     def test_is_palindrome_all_false(self):
#         assert self.palindrome.is_palindrome_all("python") == False

#     def test_is_palindrome_slicing(self):
#         assert self.palindrome.is_palindrome_slicing("anna") == True
#         assert self.palindrome.is_palindrome_slicing("Anna") == True

#     def test_is_palindrome_slicing_false(self):
#         assert self.palindrome.is_palindrome_slicing("python") == False

#     def test_is_palindrome_reverse(self):
#         assert self.palindrome.is_palindrome_reverse("anna") == True
#         assert self.palindrome.is_palindrome_reverse("Anna") == True

#     def test_is_palindrome_reverse_false(self):
#         assert self.palindrome.is_palindrome_reverse("python") == False
