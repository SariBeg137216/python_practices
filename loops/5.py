num = int(input("enter your num: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Total digits are: ", count)