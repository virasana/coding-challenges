
n = 17
# bin will be the longest - get the padding from len(bin(n))
padding = len(bin(n))
# use f string to convert the number to a string representation
print(f'{n}'.rjust(padding)) # decimal
print(f'{oct(n)}'.rjust(padding))
print(f'{hex(n)}'.rjust(padding))
print(f'{bin(n)}'.rjust(padding))

print(f'{n:{padding}} {n:{padding}o} {n:{padding}X} {n:{padding}b}')

