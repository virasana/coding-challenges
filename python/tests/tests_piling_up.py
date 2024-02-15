import unittest, sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(current_dir, '..')
sys.path.append(project_dir)

from src.challenges.piling_up import solve

class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertTrue(solve('4 3 2 1 3 4'))  # Can be piled up
        self.assertFalse(solve('1 3 2'))  # Cannot be piled up
        self.assertTrue(solve('1 1 1 1'))  # All cubes are the same size
        self.assertTrue(solve('4 3 2 1 2 3'))  # Cannot be piled up

if __name__ == '__main__':
    unittest.main()