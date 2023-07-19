# Thomas Cholak
import difflib
# Problem 8

from itertools import permutations
import enchant

d = 2

eng_dict = enchant.Dict("en_US")
op = set()

inp = input("Please enter a string: ")
# inp = "extreme"
lettr = [x.lower() for x in inp]

for n in range(d+1, len(inp)):
    for y in list(permutations(lettr, d+1)):
        z = "".join(y)
        if eng_dict.check(z):
            op.add(z)

print(f'Possible 3-letter words are:\n  {op}')

