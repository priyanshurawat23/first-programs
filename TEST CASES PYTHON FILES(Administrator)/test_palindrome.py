import unittest
from PALINDROME_CHECKER import is_palindrome

class TestPalindromeFunction(unittest.TestCase):
    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("Hello, World!"))

    def test_is_palindrome_ignore_case(self):
        self.assertTrue(is_palindrome("Racecar"))

    def test_is_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))

if __name__ == '__main__':
    unittest.main()
