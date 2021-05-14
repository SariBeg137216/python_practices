"""Remove duplicate from a list and create a tuple and find the minimum and maximum number"""

sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
new_list = [i for i in sampleList if sampleList.count(i) != 2]
print(min(new_list), max(new_list))
print(tuple(new_list))

