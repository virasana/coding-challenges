import re
string = 'AbCDe_'

# isalnum ==> includes the underscore
print(any(ch.isalnum() for ch in string)) # uses any(list(bool))
print(re.search(r'[A-Za-z_]', string) is not None)  # no 'any' as this is a regex




