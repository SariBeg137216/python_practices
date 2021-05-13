number_of_terms = 5
nums = 2
sums = 0
for i in range(number_of_terms+1):
    print(nums)
    sums += nums
    nums = (nums * 10) + 2

print(sums)
