str1 = "Apple"
result = dict()

for char in str1:
    count = str1.count(char)
    result[char] = count
print(result)

str1 = "PYnative"
print(str1[::-1])

str1 = "Emma is a data scientist who knows Python. Emma works at google."
print(str1.rfind("Emma"))
str1 = "Emma-is-a-data-scientist"
for char in str1.split("-"):
    print(char)

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_list = list(filter(None, str_list))

for items in str_list:
    if items == "" and items is None:
        str_list.remove(items)

print(str_list)
print(new_list)
