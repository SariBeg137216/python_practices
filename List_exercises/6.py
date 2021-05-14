"""Add item 7000 after 6000 in the following Python List"""
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
new_list = list1[2][2]
new_list.append(7000)
print(new_list)
print(list1)