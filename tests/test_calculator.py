import unittest

from app.calculator import (
    add_numbers,
    divide_numbers,
    multiply_numbers,
    power_numbers,
    subtract_numbers,
)


class TestAddNumbers(unittest.TestCase):
    def test_adds_two_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_adds_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_adds_floats(self):
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3)


class TestOtherOperations(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract_numbers(7, 4), 3)

    def test_multiply(self):
        self.assertEqual(multiply_numbers(6, 5), 30)

    def test_divide(self):
        self.assertEqual(divide_numbers(8, 2), 4)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide_numbers(1, 0)

    def test_power(self):
        self.assertEqual(power_numbers(2, 10), 1024)


if __name__ == "__main__":
    unittest.main()
