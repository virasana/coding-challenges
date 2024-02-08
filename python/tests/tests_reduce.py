import os, sys, unittest
from fractions import Fraction

current_dir = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from src.challenges.reduce import product

class TestReduce(unittest.TestCase):
    def test_product(self):
        # Test case 1: Product of fractions
        fracs = [Fraction(1, 2), Fraction(3, 4), Fraction(5, 6)]
        expected = (5, 16)
        actual = product(fracs)
        self.assertEqual(actual, expected, "Test case 1 failed")

        # Test case 2: Product of fractions with whole numbers
        fracs = [Fraction(1, 2), Fraction(2, 1), Fraction(3, 1)]
        expected = (3, 1)
        actual = product(fracs)
        self.assertEqual(actual, expected, "Test case 2 failed")

        # Test case 3: Product of fractions with negative numbers
        fracs = [Fraction(-1, 2), Fraction(3, 4), Fraction(5, 6)]
        expected = (-5, 16)
        actual = product(fracs)
        self.assertEqual(actual, expected, "Test case 3 failed")
