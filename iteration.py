
range_end_num = int(input("enter range end number: "))

for i in range(range_end_num + 1):
    if i == 0:
        previous_number = 0
        current_number = 0
    else:
        current_number = i
        previous_number = i - 1
    print("the current number is {} and sum by previous num is {}".format(i, current_number + previous_number))




