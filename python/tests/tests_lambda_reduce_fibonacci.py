# tests/test_lambda_fibonacci.py

import unittest, sys, os

current_dir = os.path.dirname(__file__)
project_dir = os.path.join('..', current_dir)
sys.path.append(project_dir)
module = __import__(__name__) # We are importing get_fib 
# into the local module, so we need a reference to local 
# module in order to use getattr below

from src.challenges.lambda_fibonacci import get_fib
from src.challenges.lambda_fibonacci import get_fib_1

class TestGetFib(unittest.TestCase):
    def test_get_fib(self):
        functions = ['get_fib', 'get_fib_1'] # test both implementations
        for function in functions:
            get_fib = getattr(module, function)
            # Test with n = 0
            expected = []
            actual = get_fib(0)
            self.assertEqual(actual, expected)

            # Test with n = 1
            expected = [0]
            actual = get_fib(1)
            self.assertEqual(actual, expected)

            # Test with n = 2
            expected = [0, 1]
            actual = get_fib(2)
            self.assertEqual(actual, expected)

            # Test with n = 5
            expected = [0, 1, 1, 2, 3]
            actual = get_fib(5)
            self.assertEqual(actual, expected)

            # Test with n = 10
            expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
            actual = get_fib(10)
            self.assertEqual(actual, expected)

            # Test with negative n
            with self.assertRaises(IndexError):
                get_fib(-1)

if __name__ == '__main__':
    unittest.main()