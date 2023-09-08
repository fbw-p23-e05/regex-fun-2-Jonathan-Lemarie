# -- Write a Python program to find the substrings within a string.

import re

Sample_text = 'Python exercises, PHP exercises, C# exercises'

Pattern = 'exercises'


result = re.findall(Pattern, Sample_text)
print(result)

# i don't understand how they are 2 instances, when it seems to be 3