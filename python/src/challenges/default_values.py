class MyClass:
    def my_method(self, my_variable="My Class"):
        print(my_variable)

class YourClass:
    def my_method(self, my_variable="Your Class "):
        print(my_variable)

def do_something(some_class=MyClass()):
    some_class.my_method()

do_something()
do_something(YourClass())
do_something()


    


