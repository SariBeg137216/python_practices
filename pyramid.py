def pyramid(number):
    for i in range(number):
        for j in range(0, i+1):
            print(i, end=" ")

        print("\r")


pyramid(6)

for num in range(10):
    for i in range(num):
        print(num, end=" ")  #print number
    # new line after each row to display pattern correctly
    print("\n")


