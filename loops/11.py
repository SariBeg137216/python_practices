num1 = 0
num2 = 1
for i in range(0, 11):
    temp = num1
    num1 = num2
    num2 = temp + num1
    print(temp)
