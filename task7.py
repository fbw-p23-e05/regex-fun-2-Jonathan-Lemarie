
# - - Write a Python program to replace whitespaces with an underscore and vice versa.

import re

input_string = ' _The quick brown _fox jumps over the_lazy dog_.'

# Replace spaces with a temporary placeholder character
temp_placeholder = '#'
temp_string = re.sub(r' ', temp_placeholder, input_string)
#print(temp_string)

# Replace underscores with spaces
temp_string = re.sub(r'_', r' ', temp_string)
#print(temp_string)

# replace temp_placeholder with underscore
swapped_result = re.sub(temp_placeholder, '_', temp_string)
print(swapped_result)

