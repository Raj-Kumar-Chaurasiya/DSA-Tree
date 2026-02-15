class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

first = Node(2)
second = Node(3)
third = Node(4)
fourth = Node(5)

first.left = second
first.right = third
second.left = fourth