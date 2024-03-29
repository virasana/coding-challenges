import sys, os, unittest

current_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.join(current_dir, '..')
sys.path.append(project_dir)

from src.challenges.iterables_and_iterators import get_probability

class TestIterables(unittest.TestCase):
    def test_get_probability(self):
        # Test case 1: Probability of 'a' in 2-letter combinations
        N = 4
        letters = 'a a c d'
        K = 2
        expected = 0.8333333333333334
        actual = get_probability(N, letters, K)
        self.assertAlmostEqual(actual, expected, places=7)

        # Test case 2: Probability of 'a' in 1-letter combinations
        N = 4
        letters = 'a a c d'
        K = 1
        expected = 0.5
        actual = get_probability(N, letters, K)
        self.assertAlmostEqual(actual, expected, places=7)

        # Edge case 1: Empty string
        N = 0
        letters = ''
        K = 0
        expected = 0 
        actual = get_probability(N, letters, K)
        self.assertAlmostEqual(actual, expected, places=7)

        # Edge case 2: Single letter, 'a' not present
        N = 1
        letters = 'b'
        K = 1
        expected = 0.0  # 'a' cannot be in the combination as it's not present
        actual = get_probability(N, letters, K)
        self.assertAlmostEqual(actual, expected, places=7)

        # Edge case 3: All 'a's
        N = 3
        letters = 'a a a'
        K = 2
        expected = 1.0  # 'a' will always be in the combination as all letters are 'a'
        actual = get_probability(N, letters, K)
        self.assertAlmostEqual(actual, expected, places=7)
