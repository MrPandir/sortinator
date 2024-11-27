import unittest

from src.utils import parse_input


class TestUtils(unittest.TestCase):
    def test_parse_input_valid_numbers(self):
        """Test parsing valid integer numbers."""
        self.assertEqual(parse_input("1,2,3"), [1, 2, 3])
        self.assertEqual(
            parse_input("  1\t, 2, 3   ,"), [1, 2, 3]
        )  # Strips extra spaces around numbers

    def test_parse_input_empty_values(self):
        """Test that empty values are ignored."""
        self.assertEqual(parse_input("1,,2"), [1, 2])

    def test_parse_input_non_numeric_strings(self):
        """Test that non-numeric strings are ignored."""
        self.assertEqual(parse_input("a,b,c"), [])
        self.assertEqual(parse_input("1A,2,3Q,"), [2])

    def test_parse_input_float_values(self):
        """Test that float values are ignored."""
        self.assertEqual(parse_input("1.0, 2.5, 3.8"), [])
        self.assertEqual(parse_input("4.0, 5.0, 6"), [6])

    def test_parse_input_mixed_values(self):
        """Test that mixed float and integer values are handled correctly."""
        self.assertEqual(parse_input("1, 2.1, 3"), [1, 3])

    def test_parse_input_negative_numbers(self):
        """Test that negative numbers are ignored."""
        self.assertEqual(parse_input("-6"), [])
        self.assertEqual(parse_input("-7, -8, 9"), [9])
        self.assertEqual(parse_input("10, -11, -12"), [10])


if __name__ == "__main__":
    unittest.main()
