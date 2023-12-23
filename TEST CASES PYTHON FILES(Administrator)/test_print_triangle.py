import unittest
from io import StringIO
import sys
from print_triangle import print_triangle

def get_printed_output(rows):
    captured_output = StringIO()
    sys.stdout = captured_output
    print_triangle(rows)
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()

class TestPrintTriangle(unittest.TestCase):
    def test_print_triangle_3_rows(self):
        # Test with 3 rows
        rows = 3
        actual_output = get_printed_output(rows)
        expected_output = "  * \n * * \n* * *"
        self.assertEqual(actual_output, expected_output.strip())

    def test_print_triangle_5_rows(self):
        # Test with 5 rows
        rows = 5
        actual_output = get_printed_output(rows)
        expected_output = "    * \n   * * \n  * * * \n * * * * \n* * * * *"
        self.assertEqual(actual_output, expected_output.strip())

if __name__ == '__main__':
    unittest.main()
