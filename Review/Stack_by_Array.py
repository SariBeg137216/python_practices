class Node:

    def __init__(self, data):
        self.data = data


class STACKBYArray:

    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)

    def Pop(self):
        try:
            self.array.pop()
        except IndexError:
            raise

    def printing(self):
        print(self.array)


if __name__ == "__main__":

    x = STACKBYArray()
    x.push(10)
    x.push(20)
    x.Pop()
    x.Pop()
    x.Pop()
    x.printing()
