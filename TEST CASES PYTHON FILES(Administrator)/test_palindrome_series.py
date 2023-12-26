import unittest

from your_script_file import is_palindrome, generate_palindromes

class TestPalindromeFunctions(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(1221))
        self.assertTrue(is_palindrome(12321))
        self.assertFalse(is_palindrome(12345))

    def test_generate_palindromes(self):
        self.assertEqual(generate_palindromes(5), [1, 2, 3, 4, 5])
        self.assertEqual(generate_palindromes(10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(generate_palindromes(0), [])

if __name__ == '__main__':
    unittest.main()
