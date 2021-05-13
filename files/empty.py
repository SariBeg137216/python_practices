import os

print(os.stat("test.txt").st_size == 0)


def file_size(filename):
    size = os.path.getsize(filename=filename)
    if size == 0:
        print("file is empty")
    else:
        print(size)


file_size("hello.txt")
