str1 = "SaTulPW"
new_str_lower = ""
new_str_upper = ""
for i in str1:
    if i.islower():
        new_str_lower += i
    elif i.isupper():
        new_str_upper += i

print(new_str_lower + new_str_upper)