# test_print_word_uppercase.py

import unittest
from io import StringIO
import sys
from print_word_uppercase import print_word_uppercase

class TestPrintWordUppercase(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        self.held_output.close()
        sys.stdout = sys.__stdout__

    def capture_output(self):
        return self.held_output.getvalue().strip()

    def test_print_word_uppercase_example(self):
        print_word_uppercase("example")
        result = self.capture_output()
        self.assertEqual(result, "E\nEX\nEXA\nEXAM\nEXAMP\nEXAMPL\nEXAMPLE")

    def test_print_word_uppercase_hello(self):
        print_word_uppercase("hello")
        result = self.capture_output()
        self.assertEqual(result, "H\nHE\nHEL\nHELL\nHELLO")

    def test_print_word_uppercase_single_letter(self):
        print_word_uppercase("a")
        result = self.capture_output()
        self.assertEqual(result, "A")

    def test_print_word_uppercase_empty_string(self):
        print_word_uppercase("")
        result = self.capture_output()
        self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()
