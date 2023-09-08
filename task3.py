
# -- Task 3 - Write a Python program to search for literal strings within a string. Sample text : 'The quick brown fox jumps over the lazy dog.' Searched words : 'fox', 'dog', 'horse'

import re


string = 'The quick brown fox jumps over the lazy dog.'

words_to_search = ['fox', 'dog', 'horse']

pattern = '|'.join(re.escape(word)for word in words_to_search)

result = re.findall(pattern, string)
print(result)

# other way to print the result.
for word in words_to_search:
    if word in string:
        print(word, 'found in string')
    else:
            print(word, ' not found in string')

