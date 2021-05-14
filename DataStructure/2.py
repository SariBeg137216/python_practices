"""
Given a list, remove the element at index 4 and add it to the 2nd position and at the end of the list
"""

list1 = [54, 44, 27, 79, 91, 41]
item_index4 = list1.pop(4)
add_to_index2 = list1.insert(2, item_index4)
add_to_end = list1.append(item_index4)
print(list1)