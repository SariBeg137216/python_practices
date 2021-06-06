class Node:

    def __init__(self, data):
        self.data = data


class QUEUE:

    def __init__(self):
        self.array = []

    def add(self, data):
        new = Node(data)
        self.array.append(new.data)

    def deldata(self):
        self.array.pop(0)

    def printing(self):
        print(self.array)


if __name__ == "__main__":

    x = QUEUE()
    x.add(10)
    x.add(20)
    x.add(30)
    x.deldata()
    x.printing()
