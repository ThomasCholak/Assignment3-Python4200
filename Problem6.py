# Thomas Cholak

# Problem 6

rand_string = "Amidst the bustling city streets, the curious cat " \
              + "gracefully leaped over the shimmering puddles, " \
              + "chasing shadows cast by flickering lampposts " \
              + "while murmuring melodies of forgotten tales, weaving " \
              + "dreams into the tapestry of moonlit nights, as whispers " \
              + "of enchantment danced with the scent of jasmine, " \
              + "transcending time and embracing the infinite mysteries " \
              + "that lay within the cosmos."

new_str = rand_string.split()  # splits string into an array


def reverse_string(m):
    new_str2 = m[::-1]  # reverses tokens in array
    print("Reversed string:\n", new_str2, "\n")


def find_d(n):
    new_str3 = [i for i in n if i.lower().startswith("d")]  # searches for letter d at index[0]
    print("Words beginning with 'd'\n", new_str3, "\n")


def find_ing(p):
    new_str4 = [i for i in p if i.lower().endswith("ing")]
    print("Words ending with '-ing'\n", new_str4)


reverse_string(new_str)  # reverse string function
find_d(new_str)          # finds words beginning with 'd'
find_ing(new_str)        # finds words ending with '-ing.'
