# Thomas Cholak

# Problem 2
import numpy as np

d = 3
numbers = np.arange(1, 16, 1).reshape(d, d + 2)  # creates array 1-15

values1 = (numbers[:, [0, 2, d]]).flatten()  # grabs columns for problem F
values2 = (numbers[[1, 2], :]).flatten().tolist()  # grabs rows for problem F

print(f'd = {d}')

print("Original array:")
print(numbers)

# A
print("\nRow d-1:")
print(numbers[d - 1, :])

# B
print("\nColumn d:")
print(numbers[:, d])

# C
print("\nRows 0 and 1:")
print(numbers[[0, 1], :])

# D
print("\nColumns 2-d:")
print(numbers[:, 2 - d])

# E
print("\nElement in row 1 and column d:")
print(numbers[1, d])

# F
print("\nAll elements from rows 1 and "
      + "2 that are in columns 0, 2, and d:")
print(np.intersect1d(values1, values2).tolist())  # compares arrays for matching values

