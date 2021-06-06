# sums = 0
# for i in range(11):
#     sums += i
# print(sums)
#

def sums(num):
    if num:
        return num + sums(num - 1)
    else:
        return 0


print(sums(10))
