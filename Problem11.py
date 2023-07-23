# Thomas Cholak

# Problem 11

import re

# Problem B
# used a website to randomly generate the string 'str_rand' below
str_rand = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
           + "Sed eget mauris ac nisl hendrerit mattis. Nulla facilisi. " \
           + "Ut eget venenatis dui. Integer egestas mauris vitae erat bibendum, " \
           + "email@example.com pharetra lorem@example.net eget, semper ligula@example.org. " \
           + "Aliquam erat volutpat. Nam maximus fringilla mauris, ut euismod justo@example.co.uk facilisis quis. " \
           + "Fusce suscipit magna@example.info nec orci ornare, ut tincidunt nulla@example.us consequat. " \
           + "Nulla facilisi. Suspendisse potenti. Donec auctor ante sit amet dui tristique, " \
           + "email2@example.org quis rutrum@example.com risus iaculis. " \
           + "Quisque at eros vel libero scelerisque gravida."

new_str = re.split(r"\s+", str_rand)  # splits string via regex


def find_email(m):
    r = re.compile(r'[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+')  # regex for text seperated by '@' sign
    new_str2 = list(filter(r.match, m))
    print("E-mail addresses: \n", new_str2, "\n")


find_email(new_str)
