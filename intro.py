import numpy as np

list1 = [1, 2, 3, 4, 5]
# print(list1)
# print(list1[4])

np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(np1)

# shape of numeric-pythonarray = length in array
# print(np1.shape)

# Range
# builds a np array with 10 items start from 0
np2 = np.arange(10)
# print(np2)


# np3 = np.arange(100)
# print(np3)

# Step
np4 = np.arange(0, 10, 2)
# print(np4)
# prints [0 2 4 6 8]

# Zeros
np5 = np.zeros(100)
# print(np5)

# Multidimensional zeros array
np6 = np.zeros((2, 10))
print(np6)

# Full
np7 = np.full((3, 10), 6.3)
print(np7)

# Convert Python lists to np
my_list = [1,2,3,4,5]
np8 = np.array(my_list)
print(np8)

# Numpy used in scikit-learn / panda

