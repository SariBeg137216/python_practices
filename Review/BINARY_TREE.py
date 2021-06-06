class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarYTree:

    def __init__(self):
        self.root = None

    # def printing(self):
    #     node = self.root
    #     while node:
    #         if node.left:
    #             print(node.left.data)
    #         else:
    #             print(node.right.data)
    #         node = node.right

    def insertion(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insertion(self.root, data)

    def _insertion(self, node, data):
        new_data = Node(data)
        if node.data > new_data.data:
            if node.left is None:
                node.left = new_data
            else:
                self._insertion(node.left, data)
        if node.data < new_data.data:
            if node.right is None:
                node.right = new_data
            else:
                self._insertion(node.right, data)

        elif node.data == new_data.data:
            return node.data

    def find(self, data):
        if self.root:
            is_fOund = self._find(self.root, data)
            if is_fOund:
                return True
            return False
        else:
            return print("No data in Tree, Tree is empty")

    def _find(self, node, data):
        if data < node.data and node.left:
                return self._insertion(node.left, data)
        elif data > node.data and node.right:
                return self._insertion(node.right, data)
        if data == node.data:
            return True

    def delete(self, data):
        return self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node
        elif data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left and node.right is None:
                return None
            elif node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                minValue = min(node.right)
                node.data = minValue
                node.right = self._delete(node.right, minValue)


if __name__ == "__main__":
    x = BinarYTree()
    x.root = Node(10)
    x.insertion(4)
    x.insertion(8)
    print(x.find(4))
    print(x.find(6))
    x.delete(8)
