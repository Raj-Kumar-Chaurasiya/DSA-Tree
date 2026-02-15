class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        root = Node(data)
    else:
        root.right = insert(root.right, data)
    return root

def printTree(node):
    if node is not Node:
        print(node.data)
        printTree(node.right)

root = None
root = insert(root, 1)
insert(root,2)
insert(root, 3)
insert(root, 4)
insert(root, 5)

printTree(root)