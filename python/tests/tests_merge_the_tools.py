import unittest, os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_dir)

import src.challenges.merge_the_tools as merge

class TestMergeTheTools(unittest.TestCase):
    def test_merge_the_tools(self):
        # Test case 1: Example from the problem statement
        string1 = "AABCAAADA"
        k1 = 3
        expected1 = ["AB", "CA", "AD"]
        actual1 = merge.merge_the_tools(string1, k1)
        self.assertEqual(actual1, expected1)

        # Test case 2: String length is not divisible by k
        string2 = "ABCDE"
        k2 = 2
        expected2 = ["AB", "CD", "E"]
        actual2 = merge.merge_the_tools(string2, k2)
        self.assertEqual(actual2, expected2)

        # Test case 3: All characters in the string are the same
        string3 = "AAAAA"
        k3 = 2
        expected3 = ["A", "A", "A"]
        actual3 = merge.merge_the_tools(string3, k3)
        self.assertEqual(actual3, expected3)

        # Test case 4: Empty string
        string4 = ""
        k4 = 3
        expected4 = []
        actual4 = merge.merge_the_tools(string4, k4)
        self.assertEqual(actual4, expected4)

        # Test case 5: k == 0
        string4 = ""
        k4 = 0
        expected4 = []
        actual4 = merge.merge_the_tools(string4, k4)
        self.assertEqual(actual4, expected4)

if __name__ == '__main__':
    unittest.main()