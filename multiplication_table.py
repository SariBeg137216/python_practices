def multiply(num):
    for i in range(1, num+1):
        for j in range(1, num+1):
            print(i * j, end=" ")

        print("\n")


multiply(10)