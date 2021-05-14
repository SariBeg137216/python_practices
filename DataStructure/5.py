"""Given a two list of equal size create a Python set such that it shows the element from both lists in the pair"""

list1 = [2, 3, 4, 5, 6, 7, 8]
list2 = [4, 9, 16, 25, 36, 49, 64]
my_set = set()
for i in zip(list1, list2):
    my_set.add(i)

print(my_set)




