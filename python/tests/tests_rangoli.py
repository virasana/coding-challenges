from io import StringIO
import os
import sys
import unittest
from unittest.mock import patch

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from src.challenges.rangoli import get_rangoli

class TestGetRangoli(unittest.TestCase):
    def test_get_rangoli(self):
        actual = get_rangoli(3)
        expected = ['----c----', '--c-b-c--', 'c-b-a-b-c', '--c-b-c--', '----c----']
        self.assertEqual(actual, expected)

        actual = get_rangoli(1)
        expected = ['a']
        self.assertEqual(actual, expected)

        actual = get_rangoli(2)
        expected = ['--b--', 'b-a-b', '--b--']
        self.assertEqual(actual, expected)

    def test_get_rangoli_zero(self):
        actual = get_rangoli(0)
        expected = []
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()