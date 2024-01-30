import sys

def reverse_string(text):
    print("reverse_string", file=sys.stderr)
    return text[::-1]

def is_palindrome(text):
    return text == reverse_string(text)