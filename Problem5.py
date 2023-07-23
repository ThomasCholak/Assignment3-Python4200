# Thomas Cholak

# Problem 5

import pandas as pd

# A
temperatures = {
    "Maxine": [100, 101, 80],
    "James": [50, 40, 45],
    "Amanda": [30, 70, 20]
}

# B
temp_format = pd.DataFrame(temperatures, index=["Morning", "Afternoon", "Evening"])

print(temp_format)

# C
print(f'\nThe values for \'Maxine\' are:\n{temp_format["Maxine"]}')

# D
print(f'\nThe values for \'Morning\' are:\n{temp_format.loc["Morning"]}')

# E
print(f'\nThe values for \'Morning\' and \'Evening\' are:\n{temp_format.loc[["Morning", "Evening"]]}')

# F
print(f'\nThe values for \'Amanda\' and \'Maxine\' are:\n{temp_format[["Amanda", "Maxine"]]}')

# G
print(f'\nThe values for rows \'Morning\' and \'Evening\''
      + f' and columns \'Amanda\' and \'Maxine\'\n'
      + f'{temp_format.loc[["Morning", "Afternoon"], ["Amanda", "Maxine"]]}\n')

# H
print(temp_format.describe())

# I
df_transpose = temp_format.T  # transposes the data
print(f'\nTransposed data:\n{df_transpose}')

# J
temp_format = temp_format.reindex(sorted(temp_format.columns), axis=1)  # sorts alphabetically
print(f'\nAlphabetically sorted:\n{temp_format}')
