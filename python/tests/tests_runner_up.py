import os, sys, unittest

current_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_dir)

from src.challenges.runner_up import find_runner_up

class TestRunnerUp(unittest.TestCase):
    def test_runner_up(self):
        # Test case 1: Array with duplicate values
        arr = [2, 3, 6, 6, 5]
        expected = 5
        actual = find_runner_up(arr)
        self.assertEqual(actual, expected)

        # Test case 2: Array with unique values
        arr = [1, 2, 3, 4, 5]
        expected = 4
        actual = find_runner_up(arr)
        self.assertEqual(actual, expected)

        # Test case 3: Array with negative values
        arr = [-1, -2, -3, -4, -5]
        expected = -2
        actual = find_runner_up(arr)
        self.assertEqual(actual, expected)