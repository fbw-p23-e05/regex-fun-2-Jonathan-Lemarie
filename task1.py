
# -- task 1 -- Write a Python program to check for a number at the end of a string.

import re

pattern = '\d$'


sentence_1 = 'Today is july 18'

print(re.search(pattern, sentence_1))

if re.search(pattern, sentence_1):
    print('pattern found within the string')
else:
    print('no pattern fitting within the string')



sentence_2 = 'Today is 18 july '

print(re.search(pattern, sentence_2))   

if re.search(pattern, sentence_2):
    print('pattern found within the string')
else:
    print('no pattern fitting within the string')



sentence_3 = input('Enter your sentence here: ')

if re.search(pattern, sentence_3):
    print('pattern found within the string')
else:
    print('no pattern fitting within the string')