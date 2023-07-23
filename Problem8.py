# Thomas Cholak

# Problem 8

from itertools import permutations
import enchant

eng_dict = enchant.Dict("en_US")
op = set()

test = True

d = int(input("Please input an integer for d:"))

while test:
    inp = input(f"Please enter a {d*2}-letter string: ")
    if len(inp) == d*2:
        test = False


lettr = [x.lower() for x in inp]

for n in range(d+1, len(inp)):                    # used for-loop from https://www.youtube.com/watch?v=nLWi-2b_OjE
    for y in list(permutations(lettr, (d*2)-1)):  # lists all possible word combinations
        z = "".join(y)
        if eng_dict.check(z):                     # checks permutation against the english dictionary
            op.add(z)                             # if a match is found, it's added to the 'op' list

print(f'Possible {(d*2)-1}-letter words are:\n  {op}')

