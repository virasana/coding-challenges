import os, sys, unittest

current_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_dir)

from src.challenges.list_comprehensions import get_cuboid_permuations

class TestListComprehensions(unittest.TestCase):
    def test_get_cuboid_permuations(self):
        # Test case 1: Small cuboid
        expected = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
        actual = get_cuboid_permuations(1, 1, 1, 2)
        self.assertEqual(actual, expected)

        # Test case 2: Larger cuboid
        expected = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 2, 0], [0, 2, 2], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2], [1, 2, 1], [1, 2, 2], [2, 0, 0], [2, 0, 2], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
        actual = get_cuboid_permuations(2, 2, 2, 3)
        self.assertEqual(actual, expected)

        # Test case 3: From Hacker Rank
        expected = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
        actual = get_cuboid_permuations(2, 2, 2, 2)
        self.assertEqual(actual, expected)
