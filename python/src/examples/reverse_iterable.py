import numpy as np

string = 'abcde'
for s in string[::-1]:
    print(s)

arr = [1,2,3,4,5,6,7,8,9,0]
print(arr[::-1])

arr.reverse() # slow and mutates arr
print(arr)

arr = [1,2,3,4,5,6,7,8,9,0] # reset the array
arr = np.array(arr) 
print(np.flipud(arr)) # use numpy.flipud (flip upside-down)