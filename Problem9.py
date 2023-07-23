# Thomas Cholak

# Problem 9

import re  # imports regex

rand_string = "Amidst the bustling city streets, the curious cat " \
              + "gracefully leaped over the shimmering puddles, " \
              + "chasing shadows cast by flickering lampposts " \
              + "while murmuring melodies of forgotten tales, weaving " \
              + "dreams into the tapestry of moonlit nights, as whispers " \
              + "of enchantment danced with the scent of jasmine, " \
              + "transcending time and embracing the infinite mysteries " \
              + "that lay within the cosmos."

new_str = re.split(r"\s+", rand_string)  # splits string via regex


def find_d(m):
    r = re.compile(r'^d')  # regex to find words beginning with 'd'
    new_str2 = list(filter(r.match, m))
    print("Words beginning with 'd'\n", new_str2, "\n")


def find_ing(n):
    r = re.compile(r'\b(\w+ing)\b')
    new_str3 = list(filter(r.match, n))
    print("Words ending with '-ing'\n", new_str3)


find_d(new_str)  # finds words beginning with 'd'
find_ing(new_str)  # finds words ending with '-ing.'
