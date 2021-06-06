class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class QUEUE:

    def __init__(self):
        self.head = None

    def end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = new

    def delNode(self):
        self.head = self.head.next
        return

    def printing(self):
        printValue = self.head
        while printValue:
            print(printValue.data, end=" ")
            printValue = printValue.next


if __name__ == "__main__":
    x = QUEUE()
    x.head = Node(10)
    x.end(11)
    x.end(12)
    x.delNode()
    x.printing()