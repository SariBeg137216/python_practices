class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insertion(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insertHelper(key, self.root)

    def insertHelper(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insertHelper(data, node.left)

        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insertHelper(data, node.right)
        else:
            print("value is already in tree")

    def find(self, data):
        if self.root:
            is_find = self._find(data, self.root)
            if is_find:
                return True
            return False
        else:
            return None

    def _find(self, key, node):
        if key < node.data and node.left:
            return self._find(key, node.left)
        elif key > node.data and node.right:
            return self._find(key, node.right)
        if key == node.data:
            return True

    def Preorder(self):
        self._Preorder(self.root)

    def _Preorder(self, node):
        if node:
            print(node.data, end=" ")
            self._Preorder(node.left)
            self._Preorder(node.right)

    def InOrder(self):
        self._InOrder(self.root)

    def _InOrder(self, node):
        if node:
            self._InOrder(node.left)
            print(node.data, end=" ")
            self._InOrder(node.right)

    def PostOrder(self):
        self._postOrder(self.root)

    def _postOrder(self, node):
        if node:
            self._postOrder(node.left)
            self._postOrder(node.right)
            print(node.data, end=" ")


x = BinaryTree()
x.root = Node(1)
x.root.left = Node(2)
x.root.right = Node(3)
x.root.left.left = Node(4)
x.root.left.right = Node(5)
x.root.right.left = Node(6)
x.root.right.right = Node(7)
x.PostOrder()