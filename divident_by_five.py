
def divisible_by_five(number_list):
    for i in number_list:
        if i % 5 == 0:
            print(" Divisible by five {}".format(i))
        elif i % 5 != 0:
            print(" Not divisible {}".format(i))


divisible_by_five(range(20))
