# Thomas Cholak

# Problem 4

import numpy as np
import pandas as pd

"""
m = int(input("Please enter a value for m: "))    # set value for m
d = int(input("Please enter a value for n: \n"))  # set value for d
"""

m = 10
d = 8

print(f'm = {m} and d = {d}\n')

# A
print(pd.Series([d, m, d + m, m - d]), "\n")

# B
print(pd.Series([100 * float(d), 100 * float(d), 100 * float(d), 100 * float(d), 100 * float(d)]), "\n")

# C
random_arr = pd.DataFrame(np.random.randint(0, 100, size=d * 10))
# ^^creates random integers between 1 and 100 for array size of d * 10
print(random_arr, "\n")

# D
temperature = [98.6, 98.9, 100.2, 97.9]
temp_format = pd.Series(temperature, index=["Julie", "Charlie", "Sam", "Andrea"])
print(temp_format, "\n")

# E
temp_dict = {  # creates dictionary
    'Julie': 98.6,
    'Charlie': 98.9,
    'Sam': 100.2,
    "Andrea": 97.9
}
print(pd.Series(temp_dict))
