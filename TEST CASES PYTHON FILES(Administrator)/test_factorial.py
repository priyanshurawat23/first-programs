import unittest

from factorial import calculate_factorial

class TestFactorialCalculation(unittest.TestCase):

    def test_positive_factorial(self):
        # Test when input is a positive integer
        result = calculate_factorial(5)
        self.assertEqual(result, 120, "Factorial of 5 should be 120")

    def test_zero_factorial(self):
        # Test when input is 0
        result = calculate_factorial(0)
        self.assertEqual(result, 1, "Factorial of 0 should be 1")

    def test_negative_factorial(self):
        # Test when input is a negative integer
        with self.assertRaises(ValueError):
            calculate_factorial(-3)

if __name__ == '__main__':
    unittest.main()
