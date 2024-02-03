class MyClass:
    def example_method(self):
        pass

    def __init__(self, num1="0", string1="zero", array1 = ["apple", "banana"]):
        self._num1 = num1
        self._string1 = string1
        self._array1 = array1
    
    def get_num1(self):
        return self._num1
    
    def get_string1(self):
        return self._string1
    
    def get_array1(self):
        return self._array1