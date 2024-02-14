import unittest, os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from src.challenges.swap_case import swap_case

class TestSwapCase(unittest.TestCase):
    def test_swap_case(self):
        self.assertEqual(swap_case('Hello World'), 'hELLO wORLD')
        self.assertEqual(swap_case('Python'), 'pYTHON')
        self.assertEqual(swap_case(''), '')  # Empty string
        self.assertEqual(swap_case('123'), '123')  # String with no alphabetic characters
        self.assertEqual(swap_case('AaBbCc'), 'aAbBcC')  # String with alternating case

if __name__ == '__main__':
    unittest.main()