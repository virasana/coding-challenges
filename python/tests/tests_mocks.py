import os
import sys
import unittest
from unittest.mock import Mock, MagicMock
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

import src.challenges.mocks as mocks

def this_function():
    return 5

class TestMocks(unittest.TestCase):
    def test_create_mock_instance(self):
        """
        Challenge 2: Mocking Class Instances
        Create a class with a method. 
        Write a function that takes an instance of this class as an argument 
        and returns a MagicMock object that mocks the behavior of the method.

        Note: I have chosen to demonstrate the concept within this test, 
        rather than by creating a class with a method, as the class/method will 
        add no further value to MagicMock(spec=class_under_test)
        """

        class_under_test = mocks.MyClass(2000, "two thousand", ["one", "two"])
        expected_num = 5
        expected_string = "expected"

        test_mock = MagicMock(spec=class_under_test) # here we go
        
        # demonstrate that we can override the values in class_under_test
        test_mock.get_num1.return_value = expected_num 
        test_mock.get_string1.return_value = expected_string

        self.assertEqual(test_mock.get_num1(), expected_num)
        self.assertEqual(test_mock.get_string1(), expected_string)



        