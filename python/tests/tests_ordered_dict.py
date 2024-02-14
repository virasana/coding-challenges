import unittest, sys, os
from collections import OrderedDict

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(current_dir, '..')
sys.path.append(project_dir)

from src.challenges.ordered_dict import get_prices

class TestGetPrices(unittest.TestCase):
    def test_get_prices(self):
        N = 5
        data = [
            'BANANA FRIES 12',
            'POTATO CHIPS 30',
            'APPLE JUICE 10',
            'CANDY 5',
            'APPLE JUICE 10'
        ]
        expected = OrderedDict([
            ('BANANA FRIES', 12),
            ('POTATO CHIPS', 30),
            ('APPLE JUICE', 20),
            ('CANDY', 5)
        ])
        actual = get_prices(N, data)
        self.assertEqual(actual, expected)

    def test_get_prices_empty(self):
        N = 0
        data = []
        expected = OrderedDict()
        actual = get_prices(N, data)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()