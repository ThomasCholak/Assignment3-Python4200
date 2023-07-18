# Thomas Cholak

# Problem 1

import numpy as np

d = 2  # set values for d as 2
numbers = np.arange(1, 7, 1).reshape(d, d + 1)

print(f'd = {d}')
print("D-by-D Dimensions =", numbers.shape)  # prints dimensions of array

print("\nOriginal Array:")
print(numbers)

# A
print("\nCubed Array:")
print(np.power(numbers, 3))

# B
m = int(input("\nEnter a value for m: "))
print("Array with m added")
print(np.add(numbers, m))

# C
print("\nArray multiplied by m:")
print(np.multiply(numbers, m))
