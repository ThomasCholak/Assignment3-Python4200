# Thomas Cholak

# Problem 7

import random

article = ["A", "The", "Some"]
nouns = ["pizza", "gorilla", "man", "ice-water", "puppy"]
adjectives = ["charming", "cruel", "gigantic", "huge", "tiny"]
verbs = ["drives", "swims", "gallops", "walks", "jaunts"]
prepositions = ["in", "on", "at"]

m = int(input("Please input how many sentences you'd like:\n\n"))
n = 0

while n < m:
    n += 1

    # randomly generated numbers
    rand_num1 = random.randrange(0, 5)
    rand_num2 = random.randrange(0, 3)
    rand_num3 = random.randrange(0, 5)
    rand_num4 = random.randrange(0, 3)
    rand_num5 = random.randrange(0, 5)

    print(article[rand_num2], nouns[rand_num1], verbs[rand_num1], prepositions[rand_num2],
          article[rand_num4].lower(), nouns[rand_num5] + ".")
