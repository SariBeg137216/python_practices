number_list = [1, 2, 3, 4, 5, 1]


def list_check(iter_list):
    if iter_list[0] == iter_list[-1]:
        print("True")
    else:
        print("False")


list_check(number_list)
