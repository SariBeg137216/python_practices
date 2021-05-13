input_number = 6
for i in range(1, input_number + 1):
    cube = i ** 3
    print("the cube of:  {} is {}".format(i, cube))

cu = map(lambda x: x ** 3, range(1, input_number + 1))
for i in cu:
    print(i)