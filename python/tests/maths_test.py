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
        self.assertEqual(expected, actual, msg=f'Unexpected result: {expected} != {actual}')

if __name__ == "main":
    unittest.main()


