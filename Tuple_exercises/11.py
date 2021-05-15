"""Check if all items in the following tuple are the same"""
tuple1 = (45, 45, 45, 45)
print(all(i == tuple1[0] for i in tuple1))

