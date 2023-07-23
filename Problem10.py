# Thomas Cholak

# Problem 10

import re

rand_str = "Blue 42Sunset Garden 87Lamp Table 19" \
           + "Clouds Rhythm36 River Star 91 Mountain" \
           + "23 Moonlight 68 Ocean 5"

count_digits = len(re.findall('\d', rand_str))        # counts digits
count_words = len(re.findall('[a-zA-Z]+', rand_str))  # counts words
count_non_digits = len(re.findall('\D', rand_str))    # counts non-numeric characters
count_whitespace = len(re.findall('\s', rand_str))    # counts whitespace in string

print(f'The given string is:\n   {rand_str}\n'
      + f'\nThe number of digits in this string is: {count_digits}.'
      + f'\nThe number of non-digits in this string is: {count_non_digits}.'
      + f'\nThe number of whitespaces in this string is {count_whitespace}.'
      + f'\nThe number of words in this string is: {count_words}.')
