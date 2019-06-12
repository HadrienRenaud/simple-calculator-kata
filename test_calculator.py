from unittest import TestCase
from unittest.mock import patch
from calculator import Calculator


class TestCalculator(TestCase):
    def test_add_null(self):
        self.assertEqual(Calculator.add(""), 0)

    def test_add_one(self):
        self.assertEqual(Calculator.add("1"), 1)
        self.assertEqual(Calculator.add("12.56"), 12.56)

    def test_add_two(self):
        self.assertEqual(Calculator.add("1,0"), 1)
        self.assertEqual(Calculator.add("1,2"), 3)
        self.assertEqual(Calculator.add("12,34"), 46)

    def test_add_unkwown(self):
        self.assertEqual(
            Calculator.add(','.join(map(str, range(100)))),
            100 * 99 / 2
        )
        self.assertEqual(
            Calculator.add(','.join(map(str, range(100, 201)))),
            200 * 201 / 2 - 100 * 99 / 2
        )

    def test_add_lines(self):
        self.assertEqual(
            Calculator.add('\n'.join(map(str, range(100)))),
            100 * 99 / 2
        )
        self.assertEqual(
            Calculator.add('\n'.join(map(str, range(0, 101, 2)))),
            50 * 51
        )

    def test_add_custom_separator(self):
        self.assertEqual(Calculator.add("//#\n1#2#3"), 6)
        self.assertEqual(Calculator.add("//##\n1##2##3"), 6)

    def test_add_negative(self):
        self.assertRaises(Exception, Calculator.add, ["-2"])
        self.assertRaises(Exception, Calculator.add, ["1,-2"])
        self.assertRaises(Exception, Calculator.add, ["-\n-1,-2"])

    def test_add_superior_1000(self):
        self.assertEqual(Calculator.add("2,1001"), 2)
        self.assertEqual(Calculator.add("2,1000,3"), 1005)
        self.assertEqual(
            Calculator.add(",".join(map(str, range(1200)))),
            1000 * 1001 / 2
        )

    def test_add_multiple_custom_separator(self):
        self.assertEqual(Calculator.add("//[#][%]\n1#2%3"), 6)
        self.assertEqual(Calculator.add("//[##][%%]\n1##2%%3"), 6)

    @patch('calculator.ILogger.write')
    def test_add_simple_log(self, mock_write):
        Calculator.add("1")
        mock_write.assert_called_once()

