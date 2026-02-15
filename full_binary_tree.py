class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def full(root):
    if root is None:
        return True
    
    if root.left is None and root.right is None:
        return True
    
    if root.left is not None and root.right is not None:
        return (full(root.left) and full(root.right))
    
    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(full(root))