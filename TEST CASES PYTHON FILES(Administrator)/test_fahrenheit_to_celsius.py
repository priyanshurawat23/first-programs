import unittest

from fahrenheit_to_celsius import fahrenheit_to_celsius

class TestTemperatureConversion(unittest.TestCase):

    def test_positive_conversion(self):
        # Test when input is a positive Fahrenheit temperature
        result = fahrenheit_to_celsius(32)
        self.assertEqual(result, 0, "Conversion of 32 F to Celsius should be 0 C")

    def test_negative_conversion(self):
        # Test when input is a negative Fahrenheit temperature
        result = fahrenheit_to_celsius(-40)
        self.assertEqual(result, -40, "Conversion of -40 F to Celsius should be -40 C")

    def test_zero_conversion(self):
        # Test when input is 0 Fahrenheit
        result = fahrenheit_to_celsius(0)
        self.assertEqual(result, -17.77777777777778, "Conversion of 0 F to Celsius should be approximately -17.78 C")

if __name__ == '__main__':
    unittest.main()
