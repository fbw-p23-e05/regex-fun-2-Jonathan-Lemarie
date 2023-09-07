
# -- task 4 -- Write a Python program to search for a literal string in a string and also find the location within the original string where the pattern occurs.

import re

string = 'The quick brown fox jumps over the lazy dog'

word_to_find = 'fox'

index = string.index(word_to_find, )

#position = index(word_to_find, string)

print(re.search(word_to_find, string))
print(index)

for match in index:
    position_start = match.start()
    position_end = match.end()

print('found', word_to_find, 'in', position_start, 'to', position_end)