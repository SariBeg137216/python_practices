
ip = input("Enter IP address: ")
ip += '.'
segment_length = 0
segment = 1
for char in ip:
    if char == '.':
        print("segment is {} and segment length {}".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

        char_range = char.replace(".", " ")
        print(char_range, end=" ")
