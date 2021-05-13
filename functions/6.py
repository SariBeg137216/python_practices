# num = 0
# for i in range(11):
#     num += i
# print(num)

def sum_of_numbers(n):
    if n:
        return sum_of_numbers(n-1) + n
    else:
        return 0


print(sum_of_numbers(10))


