import re
"""
return the sum and average of the digits that appear in the string, ignoring all other characters
"""


str1 = "English = 78 Science = 83 Math = 68 History = 65"
nums = re.findall("\d+", str1)
digits = []
for num in nums:
    digits.append(int(num))

print(sum(digits))
print(sum(digits) / len(digits))