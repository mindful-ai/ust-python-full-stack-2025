import unittest
from greet import greet

class TestGreet(unittest.TestCase):

    def test_greet_function(self):
        greet()

if __name__ == "__main__":

    unittest.main()

# Stops to take input from console - automation doesn't take place
# How to validate the output? Because the output is printed on console