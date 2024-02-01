from unittest.mock import Mock, MagicMock

def create_mock(some_function, return_value):
    result = Mock()
    result.return_value = return_value
    return result

class MyClass:
    def example_method(self):
        pass

    def __init__(self, num1="0", string1="zero"):
        self._num1 = num1
        self._string1 = string1
    
    def get_num1(self):
        return self._num1
    
    def get_string1(self):
        return self._string1

def create_mock(instance):
    result = MagicMock(spec=instance)
    return result