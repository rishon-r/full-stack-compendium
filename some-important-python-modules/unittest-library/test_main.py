import unittest
import main

# It is convention to create tests in a file separate from your code
# it is also convention to name them test_name_of_your_program.py

class TestCalc(unittest.TestCase): # you want to inherit from unittest.TestCase
    
    # If any of the tests fail, it wil lreturn an AssertionError

    def test_add(self): # All test methods need to start with test_ (only then will unittest.main() run all tests)
        self.assertEqual(main.add(10, 5), 15)
        self.assertEqual(main.add(-1, 1), 0) # You always wwant to ensure that you're testing all cases thoroughly, especially edge cases
        self.assertEqual(main.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(main.subtract(10, 5), 5)
        self.assertEqual(main.subtract(-1, 1), -2)
        self.assertEqual(main.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(main.multiply(10, 5), 50)
        self.assertEqual(main.multiply(-1, 1), -1)
        self.assertEqual(main.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(main.divide(10, 5), 2)
        self.assertEqual(main.divide(-1, 1), -1)
        self.assertEqual(main.divide(-1, -1), 1)
        self.assertEqual(main.divide(5, 2), 2.5)

        with self.assertRaises(ValueError): # This ensures that your exception handling is correct and that the correct errors are being raise
            main.divide(10, 0)


if __name__ == '__main__':
    # unittest.unittest.main() is a convenience function that discovers and runs all the tests in the current file when the script is executed directly
    unittest.main() # Running unittest.main() will run all tests