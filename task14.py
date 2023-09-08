
# -- Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.

import re

string = ' the Road is wide'

pattern = 'oa'

output = re.sub(pattern, '', string)
print(output)