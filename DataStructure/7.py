"""Given two sets, Checks if One Set is a subset or superset of another Set. if the subset is found delete all elements from that set"""


firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}
print(firstSet.issubset(secondSet))
print(secondSet.issuperset(secondSet))
print(secondSet.symmetric_difference(firstSet))

