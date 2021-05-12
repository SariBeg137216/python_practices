
def string_sub(char):
    string = input("Enter your string:")
    if char in string:
        print(string.count(char))
    else:
        print("{} is not in string".format(char))


string_sub("Emma")


