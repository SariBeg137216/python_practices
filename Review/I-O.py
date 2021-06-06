import os
num = 458.541315

# print("{:.2f}".format(num))


# s1, s2, s3 = input("enter your string: ").split(" ")
# print(s1, s2, s3)

# print(os.path.getsize("name.txt"))

with open('name.txt', 'r') as f:
    lines = f.readlines()
    print(lines[3])
    # for lines in f.readlines():
    #     for line in lines.split('\n'):
    #         if line == 'line4':
    #             print(line, end='')


