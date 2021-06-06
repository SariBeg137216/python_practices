class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class PRIORITY_QUEUE:

    def __init__(self):
        self.list = []

    def add(self, data):
        new = Node(data)
        self.list.append(new.data)
        self.list.sort()
        # for i in range(len(self.list)):
        #     if self.list[i] > self.list[i+1]:
        #         self.list[i], self.list[i + 1] = self.list[i + 1], self.list[i]

    def printing(self):
        print(self.list)


if __name__ == "__main__":

    x = PRIORITY_QUEUE()
    x.add(20)
    x.add(10)
    x.add(30)
    x.printing()