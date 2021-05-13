num = int(input("Enter num pyramid range : "))

for i in range(num+1):
    for j in range(num-i, 0, -1):
        print(j, end=" ")
    print()