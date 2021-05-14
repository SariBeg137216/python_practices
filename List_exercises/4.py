"""Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order"""

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i in list1:
    print(i, end=" ")
    for x in list2[::-1]:
        print(x)
        break

for x, y in zip(list1, list2[::-1]):
    print(x, y)



