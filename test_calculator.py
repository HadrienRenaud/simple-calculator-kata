from unittest import TestCase
from Calculator import Calculator


class TestCalculator(TestCase):
    def test_add_null(self):
        self.assertEqual(Calculator.add(""), 0)

    def test_add_one(self):
        self.assertEqual(Calculator.add("1"), 1)
        self.assertEqual(Calculator.add("12.56"), 12.56)

    def test_add_two(self):
        self.assertEqual(Calculator.add("1,0"), 1)
        self.assertEqual(Calculator.add("1,2"), 3)
        self.assertEqual(Calculator.add("1,-2"), -1)

    def test_add_unkwown(self):
        self.assertEqual(
            Calculator.add(','.join(map(str, range(100)))),
            100 * 99 / 2
        )
        self.assertEqual(
            Calculator.add(','.join(map(str, range(-100, 101)))),
            0
        )
