import sys, os, unittest

current_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.join(current_dir, '..')
sys.path.append(project_dir)

from src.challenges.string_mutations import mutate_string

class TestMutateString(unittest.TestCase):
    def test_mutate_string(self):
        self.assertEqual(mutate_string('abracadabra', 5, 'k'), 'abrackdabra')
        self.assertEqual(mutate_string('hello', 0, 'j'), 'jello')
        self.assertEqual(mutate_string('world', 4, '!'), 'worl!')
        self.assertEqual(mutate_string('12345', 2, '0'), '12045')

    def test_mutate_string_edge_cases(self):
        self.assertEqual(mutate_string('a', 0, 'b'), 'b')  # Single character string
        self.assertEqual(mutate_string('', 0, 'a'), 'a')  # Empty string
        with self.assertRaises(IndexError):  # Position out of range
            mutate_string('hello', 5, 'j')

if __name__ == '__main__':
    unittest.main()
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
