import challenges.strings as strings
import challenges.maths as maths

print(strings.reverse_string("hello"))
print(strings.is_palindrome("madamimadam"))
print(maths.factorial(5))
print(maths.factorial_super_duper(5))
for value in maths.factorial_generator_descending(5):
    print(value)
