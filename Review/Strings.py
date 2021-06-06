# s1 = "Ault"
# s2 = "Kelly"
# mid_s1 = len(s1) // 2
#
# s1 = s1[:mid_s1:] + s2 + s1[mid_s1::]
# print(s1)
# str1 = "Welcome to USA. usa awesome, isn't it?"
# str2 = str1.lower()
# print(str2.count("usa"))
import re

# str1 = "English = 78 Science = 83 Math = 68 History = 65"
# nums = [int(i) for i in re.findall('\d+', str1)]
# print(sum(nums))
# print(sum(nums) / len(nums))
# str1 = "Apple"
# res = dict()
# for char in str1:
#     count = str1.count(char)
#     res[char] = count
#
# print(res)


# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
#
# new_list = list(filter(None, str_list))
# print(new_list)

str1 = 'I am 25 years and 10 months old'
ls1 = []
# for char in re.findall('\d+', str1):
#     print(char, end="")

res = "".join([item for item in str1 if item.isdigit()])
print(res)

str1 = "Emma25 is Data scientist50 and AI Expert"

for c in str1:
    if c.isalpha()+c.isdigit():
        print(c)
