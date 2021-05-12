
def num_reversing(numbers):
    while numbers > 0:
        revese = numbers % 10
        numbers = numbers // 10
        print(revese, end=" ")


num_reversing(236)