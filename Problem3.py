# Thomas Cholak

# Problem 3
import numpy as np

m = 7  # set values for m as 7
d = 9  # set value for d as 9

array_1 = np.array([[0, d], [m, 3]])
array_2 = np.array([[4, 2*d], [2*m, 7]])

array_3 = np.vstack((array_1, array_2))  # A
array_4 = np.hstack((array_1, array_2))  # B
array_5 = np.vstack((array_4, array_4))  # C
array_6 = np.hstack((array_3, array_3))  # D


print("array_1:")
print(array_1)
print("array_2:")
print(array_2)

# A
print("\narray_3:")
print(array_3)

# B
print("\narray_4:")
print(array_4)

# C
print("\narray_5:")
print(array_5)

# D
print("\narray_6:")
print(array_6)
