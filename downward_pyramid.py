def down_pyramid(num):
    for i in range(num):
        for j in range(num-i):
            print("*", end="")
        print("\r")


down_pyramid(8)
