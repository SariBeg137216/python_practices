"""Remove empty strings from the list of strings"""
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
result = list(filter(None, list1))
print(result)
# for i in list1:
#     if i == "":
#         list1.remove("")
# print(list1)



