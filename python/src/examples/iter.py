string = 'abcdefghijkl' # string is iterable
i = iter(string) # get the iterable object
i = string.__iter__() # same thing but generally not recommended

print(next(i))
print(next(i))
print(next(i))
print(next(i)) # same as __next__() but generally not recommended
print('===')
for ch in i:
    print(ch)