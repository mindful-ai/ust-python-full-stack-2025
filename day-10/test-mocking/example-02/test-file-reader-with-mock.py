import unittest
from unittest.mock import mock_open, patch
from file_reader import read_first_line


class TestFileReader(unittest.TestCase):

    def test_file_read(self): # the test cases should always begin with test_<test_name>

        # create mock object
        mock_data = "Hello, World!\nSecond Line\nThird Line\n"
        m = mock_open(read_data=mock_data)

        # patch the mock object
        with patch("builtins.open", m): # patch() replaces the open() inside read_first_line()
            result = read_first_line("dummy.txt") # since open() is mocked, no file is ever read, any name can be given here

        # assertion
        self.assertEqual(result, "Hello, World")

if __name__ == "__main__":
    unittest.main(verbosity=5)