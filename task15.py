
# - - Write a Python program to replace all occurrences of a space, comma, or dot with a colon.

import re

string = str(input('enter your sentence here: '))
string_1 = ', . ,hi., ..there.,  ,., , .,'

pattern = r'[ ,.]'

result = re.sub(pattern, ':', string_1)
print(result)