import os
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

import src.challenges.maths as maths

class TestMaths(unittest.TestCase):
    def test_factorial(self):
        input = 5
        expected = 120
        actual = maths.factorial(input)
        self.assertEqual(expected, actual, f'Unexpected result: {expected} != {actual}')

    def test_factorial_super_duper(self):
        input = 5
        expected = 120
        actual = maths.factorial_super_duper(input)
        self.assertEqual(expected, actual, f'Unexpected result: {expected} != {actual}')
    
    def test_factorial_generator(self):
        expected = [20,60,120]
        for index, actual in enumerate(maths.factorial_generator_descending(5)):
            (self.assertEqual(actual, expected[index], 
                              f'Expected {expected[index]}.  Actual {actual}')
            )

    def test_fibonacci_create(self):
        expected = [0,1,1,2,3,5,8]
        actual = maths.create_fibonacci(len(expected))
        self.assertEqual(expected, actual, f'Expected: {expected}. Actual: {actual}')

    def test_fibonacci_generator(self):
        expected = [0, 1, 1, 2, 3, 5, 8]
        actual = list(maths.create_fibonacci(len(expected)))
        self.assertEqual(actual, expected, f'Expected: {expected}. Actual: {actual}')


if __name__ == "main":
    unittest.main()


