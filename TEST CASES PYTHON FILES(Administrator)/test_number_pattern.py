# test_number_pattern.py

import unittest
from io import StringIO
import sys
from number_pattern import print_number_pattern

class TestPrintNumberPattern(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        self.held_output.close()
        sys.stdout = sys.__stdout__

    def capture_output(self):
        return self.held_output.getvalue().strip()

    def test_print_number_pattern_3(self):
        print_number_pattern(3)
        result = self.capture_output()
        self.assertEqual(result, "1 \n2 1 \n3 2 1")

    def test_print_number_pattern_5(self):
        print_number_pattern(5)
        result = self.capture_output()
        self.assertEqual(result, "1 \n2 1 \n3 2 1 \n4 3 2 1 \n5 4 3 2 1")

if __name__ == "__main__":
    unittest.main()
