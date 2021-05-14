"""Reverse a given list in Python"""

aLsit = [100, 200, 300, 400, 500]
print(aLsit[::-1])


"""Concatenate two lists index-wise"""
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = zip(list1, list2)
new_list = []
for i, j in list3:
    new_list.append(i+j)
print(new_list)