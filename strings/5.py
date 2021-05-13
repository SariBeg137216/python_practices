str1 = "P@#yn26at^&i5ve"
chars = 0
digits = 0
symbols = 0
for i in str1:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        chars += 1
    else:
        symbols += 1

print("chars {}, digits {}, symbols {}".format(chars, digits, symbols))
