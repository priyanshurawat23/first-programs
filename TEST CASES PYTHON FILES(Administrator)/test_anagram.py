import unittest
from mock import patch
from ANAGRAM_STRING import get_user_input, check_anagram

class TestAnagramFunctions(unittest.TestCase):
    def test_check_anagram_positive(self):
        self.assertTrue(check_anagram("listen", "silent"))

    def test_check_anagram_negative(self):
        self.assertFalse(check_anagram("hello", "world"))

    def test_check_anagram_ignore_case(self):
        self.assertTrue(check_anagram("Tea", "Eat"))

    def test_get_user_input(self):
        user_input = "hello\nworld\n"
        with patch('builtins.input', side_effect=user_input.split('\n')):
            self.assertEqual(get_user_input(), ("hello", "world"))


if __name__ == '__main__':
    unittest.main()