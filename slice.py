import numpy as np

# slicing numpy arrays
np1 = np.array([1,2,3,4,5,6,7,8,9])

# return 2,3,4,5
# 0 is always counted
# print(np1[1:5])

# Return from something till the end of the array
# print(np1[3:])

# print(np1[-3:-1])
# prints [7 8]
# counts back from 9 as zero

# Steps
# print(np1[1:5])
# print(np1[1:5:2])

# Steps on the entire array
# print(np1[::2])
# print(np1[::3])
# print(np1[::5])

# slice a 2-d array
np2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
                    #0th row     #1th row
# pull out single item
print(np2[1,2]) # prints 8
# from the 1th row print the 2th item

# Slice a 2-d arrary 2,3
print(np2[0:1, 1:3])

# Slice from both rows
print(np2[0:2, 1:3])
