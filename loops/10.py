for i in range(25, 51):
    for x in range(2, i):
        if i % x == 0:
            print("{} Not prime".format(i))
            break
    else:
        print("{} is Prime".format(i))
