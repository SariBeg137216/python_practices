
with open('test.txt', "r+") as f:
    lines = f.readlines()
    new_line_list = []
    for line in lines:
        if line == "line5\n":
            lines.remove(line)
            print(lines)
            with open('test.txt', "w") as file:
                for items in lines:
                    file.write(items)
                    print(file)
