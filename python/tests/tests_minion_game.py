import os
import sys
import unittest
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

import src.challenges.minion_game as minion_game


class TestMinionGame(unittest.TestCase):
    def test_minion_game_fast(self):
        start_time = time.time()
        expected = 'Stuart: 12'
        expected_time = 2
        actual = minion_game.minion_game_fast('BANANA')
        self.assertEqual(actual, expected)
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.assertTrue(elapsed_time < expected_time)  # fail if the test takes more than 2 seconds

if __name__ == '__main__':
    unittest.main()
        

if __name__ == '__main__':
    unittest.main()