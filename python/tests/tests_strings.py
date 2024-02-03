import os
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

import src.challenges.strings as strings

class TestStrings(unittest.TestCase):
    def test_reverse_string(self):
        # Correctly reverses a multi-character string
        input = 'hello'
        expected = 'olleh'
        actual = strings.reverse_string(input)
        self.assertEqual(expected, actual, f'Expected: {expected}, Actual: {actual}')
        
        # Handles an empty string
        input = ''
        expected = ''
        actual = strings.reverse_string(input)
        self.assertEqual(expected, actual, f'Expected: {expected}, Actual: {actual}')
        
        # Correctly reverses a single-character string
        input = 'a'
        expected = 'a'
        actual = strings.reverse_string(input)
        self.assertEqual(expected, actual, f'Expected: {expected}, Actual: {actual}')
        
        # Correctly reverses a two-character string
        input = 'ab'
        expected = 'ba'
        actual = strings.reverse_string(input)
        self.assertEqual(expected, actual, f'Expected: {expected}, Actual: {actual}')

    def test_is_palindrome(self):
        # Correctly identifies a palindrome
        input = "radar"
        expected = (True, "radar")
        actual = strings.is_palindrome(input)
        self.assertEqual(expected, actual)
        
        # Correctly identifies a non-palindrome
        input = "python"
        expected = (False, "nohtyp")
        actual = strings.is_palindrome(input)
        self.assertEqual(expected, actual)
        
        # Considers an empty string as a palindrome
        input = ""
        expected = (True, "")
        actual = strings.is_palindrome(input)
        self.assertEqual(expected, actual, f'Expected: {expected}, Actual: {actual}')
        
        # Considers a single-character string as a palindrome
        input = "a"
        expected = (True, "a")
        actual = strings.is_palindrome(input)
        self.assertEqual(expected, actual, f'Expected: {expected}, Actual: {actual}')
        
        # Correctly identifies a two-character non-palindrome
        input = "ab"
        expected = (False, "ba")
        actual = strings.is_palindrome(input)
        self.assertEqual(expected, actual, f'Expected: {expected}, Actual: {actual}')

if __name__ == '__main__':
    unittest.main()