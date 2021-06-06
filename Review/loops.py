
# nums = 75865
# count = 0
#
# while nums != 0:
#     nums //= 10
#     count += 1
# print(count)

# for i in range(25, 51):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print("{} is prime".format(i))
#

# num1 = 0
# num2 = 1
# for i in range(10):
#     fib = num1
#     num1 = num2
#     num2 = fib + num1
#     print(fib)

# nums = 2
# number_of_terms = 5
# sums = 0
# for i in range(number_of_terms):
#     sums += nums
#     nums = (nums * 10) + 2
# print(sums)

for i in range(0, 5):
    for x in range(i+1):
        print("*", end="")
    print()
for x in range(5, 0, -1):
    for j in range(0, x-1):
        print('*', end="")
    print()
