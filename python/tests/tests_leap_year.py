import os
import sys
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

import src.challenges.leap_year as leap_year

class TestLeapYear(unittest.TestCase):
    def test_is_leap(self):
        # Test leap years
        self.assertTrue(leap_year.is_leap(2000))  # divisible by 400
        self.assertTrue(leap_year.is_leap(2400))  # divisible by 400

        # Test non-leap years
        self.assertFalse(leap_year.is_leap(1800))  # divisible by 4 and 100, but not by 400
        self.assertFalse(leap_year.is_leap(1900))  # divisible by 4 and 100, but not by 400
        self.assertFalse(leap_year.is_leap(2100))  # divisible by 4 and 100, but not by 400
        self.assertFalse(leap_year.is_leap(2200))  # divisible by 4 and 100, but not by 400
        self.assertFalse(leap_year.is_leap(2300))  # divisible by 4 and 100, but not by 400
        self.assertFalse(leap_year.is_leap(2500))  # divisible by 4 and 100, but not by 400

if __name__ == '__main__':
    unittest.main()