# def revere_number(number):
#     number = str(number)
#     reversed = number[-1:]
#     if reversed is number:
#         print("reversed {} and number is same {}".format(reversed, number))
#     else:
#         print("Not same")

def reverseCheck(number):
    print("original number", number)
    originalNum = number
    reverseNum = 0
    while number > 0:
        reminder = number % 10
        print("reminder {}".format(reminder))
        reverseNum = (reverseNum * 10) + reminder
        print("reversebum {}".format(reverseNum))
        number = number // 10
        print("number is {}".format(number))
    if originalNum == reverseNum:
        return True
    else:
        return False


print("The original and reverse number is the same:", reverseCheck(120))
