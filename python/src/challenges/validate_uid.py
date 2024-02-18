import re

def validate_string(s):
    result = True
    reasons = []
    result = result and bool(re.search(r'[A-Z].*[A-Z]', s))
    if not bool(re.search(r'[A-Z].*[A-Z]', s)):
        reasons.append('At least two uppercase letters')

    result = result and bool(re.search(r'[0-9].*[0-9]', s))
    if not bool(re.search(r'[0-9].*[0-9]', s)):
        reasons.append('At least two digits')

    result = result and bool(s.isalnum())
    if not s.isalnum():
        reasons.append('Only alphanumeric characters')

    result = result and bool(len(set(s)) == len(s))
    if not len(set(s)) == len(s):
        reasons.append('No repeated characters')

    result = result and bool(len(s) == 10)
    if not len(s) == 10:
        reasons.append('Length is 10')

    result = 'Valid' if result else 'Invalid'
    return (result, reasons)

if __name__ == '__main__':
    print(validate_string('B1CD102354'))
    print(validate_string('B1CDEF2354'))
      


