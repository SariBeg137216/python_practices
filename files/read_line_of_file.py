
with open("new_file.txt", 'r') as f:
    lines = f.readlines()
    print(lines[3])