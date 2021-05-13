import re
"""
 Remove special symbols/Punctuation from a given string
"""

str1 = "/*Jon is @developer & musician"

str2 = re.sub('\W+\s*', " ", str1)
print(str2)

