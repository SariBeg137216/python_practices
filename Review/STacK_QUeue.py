class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LInkedListSTACk:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data

    def pop(self):
        temp = self.head
        self.head = temp.next
        return

    def printing(self):
        printValue = self.head
        while printValue:
            print(printValue.data)
            printValue = printValue.next


if __name__ == "__main__":

    x = LInkedListSTACk()
    x.head = Node(10)
    x.push(9)
    x.push(8)
    x.pop()
    x.printing()