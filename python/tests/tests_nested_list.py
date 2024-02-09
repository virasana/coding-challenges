import os, sys, unittest

current_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.join(current_dir, '..')
sys.path.append(project_dir)

from src.challenges.nested_list import get_second_lowest_people

class TestNestedList(unittest.TestCase):
    def test_get_second_lowest_people(self):
        # Test case 1: List with multiple people having the second lowest score
        data = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
        expected = ['Berry', 'Harry']
        actual = get_second_lowest_people(data)
        self.assertEqual(actual, expected)

        # Test case 2: List with one person having the second lowest score
        data = [('Harry', 37.21), ('Tina', 37.2), ('Akriti', 41), ('Harsh', 39)]
        expected = ['Harry']
        actual = get_second_lowest_people(data)
        self.assertEqual(actual, expected)

        