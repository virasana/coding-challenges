import unittest
from src.challenges.count_substring import count_substring

class TestCountSubstring(unittest.TestCase):
    def test_count_substring(self):
        # Test case 1: Substring 'ab' appears twice in the string 'ababab'
        string = 'ababab'
        sub_string = 'ab'
        expected = 3
        actual = count_substring(string, sub_string)
        self.assertEqual(actual, expected)

        # Test case 2: Substring 'abc' appears once in the string 'abcdef'
        string = 'abcdef'
        sub_string = 'abc'
        expected = 1
        actual = count_substring(string, sub_string)
        self.assertEqual(actual, expected)

        # Test case 3: Substring 'xyz' does not appear in the string 'abcdef'
        string = 'abcdef'
        sub_string = 'xyz'
        expected = 0
        actual = count_substring(string, sub_string)
        self.assertEqual(actual, expected)

        # Test case 4: Substring 'aa' appears three times in the string 'aaaaa'
        string = 'aaaaa'
        sub_string = 'aa'
        expected = 4
        actual = count_substring(string, sub_string)
        self.assertEqual(actual, expected)

        # Test case 5: Substring 'a' appears five times in the string 'aaaaa'
        string = 'aaaaa'
        sub_string = 'a'
        expected = 5
        actual = count_substring(string, sub_string)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()