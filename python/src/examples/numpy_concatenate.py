import numpy as np

arr1 = np.array([
    [11, 12], 
    [13, 14], 
    [15, 16], 
    [17, 18]
                 ])
arr2 = np.array([
    [21,22], 
    [23, 24], 
    [25, 26], 
    [27, 28]])

# think of stacking by row or column respectively
print('Axis 0 i.e. rows')
# write out the rows, stacked on top of each other
print(np.concatenate((arr1, arr2), 0))
# here we stack as if we pivoted the table 90 degrees. 
# just write out the values in sequence, from the top of each column
print('Axis 1 i.e. columns')
print(np.concatenate((arr1, arr2), 1))

