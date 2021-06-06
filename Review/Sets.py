sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]

sampleSet.update(sampleList)
print(sampleSet)


set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)

set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)


set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
print(set1.isdisjoint(set2))
print(set1.intersection(set2))

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)

# set1.difference_update(set1.intersection(set2))
# print(set1)