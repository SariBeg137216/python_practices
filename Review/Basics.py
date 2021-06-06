# str = "pynative"
#
# print(str[::2])


# for i in range(6):
#     for j in range(i):
#         print(i, end='')
#     print()

def Tax(income):
    tax = 1000

    income -= 20000

    tax += income * 20 // 100

    return tax


print(Tax(60000))