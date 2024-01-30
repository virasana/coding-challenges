import os
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

import src.challenges.strings as strings

class TestStrings(unittest.TestCase):
    def test_reverse_string(self):
        input = 'hello'
        expected = 'olleh'
        actual = strings.reverse_string(input)
        self.assertEqual(expected,actual, f'Expected: {expected}, Actual: {actual}')
    def test_is_palindrome(self):
        input = 'madamimadam'
        expected = (True, "madamimadam")
        actual = strings.is_palindrome(input)
        self.assertEqual(expected, actual, f'Expected: {expected}.  Actual: {actual}')


if __name__ == "main":
    unittest.main()


