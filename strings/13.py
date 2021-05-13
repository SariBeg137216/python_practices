import re
"""Find words with both alphabets and numbers"""

str1 = "Emma25 is Data scientist50 and AI Expert"

print(re.findall('\w+\d+', str1))
