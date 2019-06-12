from unittest import TestCase
from unittest.mock import patch, MagicMock
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

    @patch('calculator.ILogger.write')
    def test_add_null_check_log(self, mock_write):
        Calculator.add("")
        mock_write.assert_called_once_with(0)

    @patch('calculator.ILogger.write')
    def test_add_one_check_log(self, mock_write):
        Calculator.add("1")
        mock_write.assert_called_once_with(1)
        mock_write.reset_mock()

        Calculator.add("12.56")
        mock_write.assert_called_once_with(12.56)
        mock_write.reset_mock()

    @patch('calculator.ILogger.write')
    def test_add_two_check_log(self, mock_write):
        Calculator.add("1,0")
        mock_write.assert_called_once_with(1)
        mock_write.reset_mock()

        Calculator.add("1,2")
        mock_write.assert_called_once_with(3)
        mock_write.reset_mock()

        Calculator.add("12,34")
        mock_write.assert_called_once_with(46)
        mock_write.reset_mock()

    @patch('calculator.ILogger.write')
    def test_add_unkwown_check_log(self, mock_write):
        Calculator.add(','.join(map(str, range(100))))
        mock_write.assert_called_once_with(100 * 99 / 2)
        mock_write.reset_mock()

        Calculator.add(','.join(map(str, range(100, 201))))
        mock_write.assert_called_once_with(200 * 201 / 2 - 100 * 99 / 2)
        mock_write.reset_mock()

    @patch('calculator.ILogger.write')
    def test_add_lines_check_log(self, mock_write):
        Calculator.add('\n'.join(map(str, range(100))))
        mock_write.assert_called_once_with(100 * 99 / 2)
        mock_write.reset_mock()

        Calculator.add('\n'.join(map(str, range(0, 101, 2))))
        mock_write.assert_called_once_with(50 * 51)
        mock_write.reset_mock()

    @patch('calculator.ILogger.write')
    def test_add_custom_separator_check_log \
                    (self, mock_write):
        Calculator.add("//#\n1#2#3")
        mock_write.assert_called_once_with(6)
        mock_write.reset_mock()

        Calculator.add("//##\n1##2##3")
        mock_write.assert_called_once_with(6)
        mock_write.reset_mock()

    @patch('calculator.ILogger.write')
    def test_add_superior_1000_check_log(self, mock_write):
        Calculator.add("2,1001")
        mock_write.assert_called_once_with(2)
        mock_write.reset_mock()

        Calculator.add("2,1000,3")
        mock_write.assert_called_once_with(1005)
        mock_write.reset_mock()

        Calculator.add(",".join(map(str, range(1200))))
        mock_write.assert_called_once_with(1000 * 1001 / 2)

    @patch('calculator.ILogger.write')
    def test_add_multiple_custom_separator_check_log(self, mock_write):
        Calculator.add("//[#][%]\n1#2%3")
        mock_write.assert_called_once_with(6)
        mock_write.reset_mock()

        Calculator.add("//[##][%%]\n1##2%%3")
        mock_write.assert_called_once_with(6)

    @patch('calculator.ILogger.write')
    def test_catching_errors_on_logger(self, mock_write):
        mock_write.side_effect = Exception("Fake Failed")
        try:
            Calculator.add("1")
        except Exception:
            self.fail()

    @patch('calculator.ILogger.write')
    @patch('calculator.IWebserver.notify')
    def test_catching_errors_on_logger(self, mock_notify, mock_write):
        mock_write.side_effect = Exception("Fake Failed")
        try:
            Calculator.add("1")
        except: pass
        mock_notify.assert_called_once()
