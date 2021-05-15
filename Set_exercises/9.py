""" Remove items from set1 that are common to both set1 and set2"""

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.difference(set1.symmetric_difference(set2)))
set1.intersection_update(set2)
print(set1)
