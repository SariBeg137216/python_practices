"""
Given two lists create a third list by picking an odd-index element from the first list and even index elements from the second.
"""


listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

oddlist1 = listOne[1::2]
evenlist2 = listTwo[::2]
oddlist1.extend(evenlist2)
print(oddlist1)