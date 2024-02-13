import unittest, sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, '..')
sys.path.append(project_root)

from src.challenges.collections_named_tuple import get_average_mark

class TestCollectionsNamedTuple(unittest.TestCase):
    def test_get_average_mark(self):
        input = [
            '5',
            'ID         MARKS      NAME       CLASS',
            '1          97         Raymond    7',
            '2          50         Pedro      9',
            '3          91         Romulo     10',
            '4          72         Abdullah   5',
            '5          80         Mark       7'
        ]
        expected = 78.0
        actual = get_average_mark(input)
        self.assertAlmostEqual(actual, expected, places=2)

        def test_same_marks(self):
            input = [
                '3',
                'ID         MARKS      NAME       CLASS',
                '1          70         Raymond    7',
                '2          70         Pedro      9',
                '3          70         Romulo     10'
            ]
            expected = 70.0
            with self.assertRaises(ValueError):
                actual = get_average_mark(input)
                self.assertAlmostEqual(actual, expected, places=2)

    def test_no_students(self):
        input = [
            '0',
            'ID         MARKS      NAME       CLASS'
        ]
        with self.assertRaises(ValueError):
            get_average_mark(input)
