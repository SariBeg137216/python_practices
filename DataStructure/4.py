"""Iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element"""


list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
result = dict()
for i in list1:
    occur = list1.count(i)
    result[i] = occur

print(result)
