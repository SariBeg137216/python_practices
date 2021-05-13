import re
"""
Removal all the characters other than integers from a string

"""

str1 = 'I am 25 years and 10 months old'
str2 = ""

for char in re.findall('\d+', str1):
    char += str2
    print(char, end="")
