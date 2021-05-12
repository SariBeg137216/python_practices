f_num = int(input("enter yor first number: "))
s_num = int(input("enter your second number: "))

product = f_num * s_num
sum_numbers = f_num + s_num


def product_return(num):

    if num > 1000:
        print("the product is greater than 1000 and its ==>{}".format(product))
        return sum_numbers
    else:
        return product


print(product_return(product))
