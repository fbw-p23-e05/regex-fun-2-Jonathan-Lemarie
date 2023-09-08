
#  -- Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon.

import re

string = str(input('enter your sentence here: '))
string_1 = ', . ,hi., ..there.,  ,., , .,'

pattern = r'[ ,.]{0,2}'  # the pattern does not fit...

result = re.sub(pattern, ':', string_1)
print(result)



