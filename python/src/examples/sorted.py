dict = {'c': 'cherry', 'z': 'cherry', 'a': 'apple', 'b': 'banana'}

keys = sorted([key for key in dict.keys()], reverse=True)
print(keys)

# item is the tuple of (key,value) - use -ord(char) to sort by single char.  
# This is less than satisfactory
print(sorted(dict.items(), key = lambda item: (item[1], -ord(item[0])))) # sort by value, key

print(sorted(dict.values(), reverse=True))
