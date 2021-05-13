import re
"""Replace each punctuation with # in the following string"""
str1 = '/*Jon is @developer & musician!!'
print(str1.split())

print(re.sub('[\W\s]', '#', str1))