import unittest
from unittest.mock import patch
from greet import greet

class TestGreet(unittest.TestCase):

    # This test case need fake input and fake output component

    @patch('builtins.input', return_value="Sunil") # <- object in mock_input: pass into test
    @patch('builtins.print')  # <- object produced will be available in mock_print: pass this also into test
    def test_greet(self, mock_print, mock_input):
        greet()
        mock_input.assert_called_once_with("Enter your name: ")
        mock_print.assert_called_once_with("Hello, Sunil")

if __name__ == "__main__":
    unittest.main()