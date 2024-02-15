# tests/test_capitalise.py
import unittest, sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join('..', current_dir)
sys.path.append(project_root)

from src.challenges.capitalise import solve

class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve('hello world'), 'Hello World')
        self.assertEqual(solve('my name is john'), 'My Name Is John')
        self.assertEqual(solve('PYTHON IS AWESOME'), 'Python Is Awesome')
        self.assertEqual(solve('123hello 123world'), '123hello 123world')
        self.assertEqual(solve(''), '')  # Empty string

if __name__ == '__main__':
    unittest.main()