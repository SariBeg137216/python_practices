def removeChars(string, num):
    if num < len(string):
        print(string[num:])
    else:
        print("the number must  be less than {}".format(len(string)))


removeChars("hello", 4)
