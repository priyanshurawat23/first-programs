import unittest
from password_generator import generate_strong_password

class TestPasswordGenerator(unittest.TestCase):

    def test_valid_password_generation(self):
        # Test when the length is greater than or equal to 4
        result = generate_strong_password(12)
        self.assertEqual(len(result), 12, "Generated password length should be 12")

    def test_invalid_password_generation(self):
        # Test when the length is less than 4
        with self.assertRaises(ValueError):
            generate_strong_password(3)

if __name__ == '__main__':
    unittest.main()
