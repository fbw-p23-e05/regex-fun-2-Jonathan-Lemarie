
# -- task 2 --  Write a Python program to search for numbers (0-9) of length between 1 and 3 in the given string. 

import re

pattern = '[0-9]{1,3}'

string = "Exercises number 1, 12, 13, and 345 are important"

print(re.findall(pattern, string))