import os
import sys
import unittest
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

import src.challenges.mocks as mocks

def this_function():
    return 5

class TestMocks(unittest.TestCase):
    def test_create_mock(self):
        # Challenge 1: Mocking Function Calls
        expected = random.random()
        
        the_mock = mocks.create_mock(this_function, 4)
        the_mock.do_something.return_value = expected

        actual = the_mock.do_something()
        self.assertEqual(expected, actual)

    def test_create_mock_instance(self):
        # Challenge 2: Mocking Class Instances
        class_under_test = mocks.MyClass(2000, "two thousand")
        expected_num = 5
        expected_string = "expected"

        test_mock = mocks.create_mock(class_under_test)
        test_mock.get_num1.return_value = expected_num
        test_mock.get_string1.return_value = expected_string

        self.assertEqual(test_mock.get_num1(), expected_num)
        self.assertEqual(test_mock.get_string1(), expected_string)



        