
def odd_even_list(ls1, ls2):
    my_list = []
    for i in ls1:
        if i % 2 == 0:
            my_list.append(i)
    for j in ls2:
        if j % 2 != 0:
            my_list.append(j)

    return sorted(my_list)


list1 = range(20)
list2 = range(10)

print(odd_even_list(list1, list2))
