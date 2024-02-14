import os
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from src.challenges.designer_door_mat import get_design

class TestGetDesign(unittest.TestCase):
    def test_get_design(self):
        margin = 4
        N = 7
        M = 21
        expected = """\
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------\
""".split('\n')
        actual = get_design(margin, N, M, expected)
        self.assertEqual(actual, '\n'.join(expected))

        N = 11
        M = 33
        expected = """\
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------\
""".split('\n')
        actual = get_design(margin, N, M, expected)
        self.assertEqual(actual, '\n'.join(expected))

if __name__ == '__main__':
    unittest.main()