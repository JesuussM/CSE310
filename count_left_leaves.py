class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_left_leaves(root):
    if root is None:
        return 0
    count = 0
    if root.left and root.left.left is None and root.left.right is None:
        count += 1
    else:
        count += count_left_leaves(root.left)
    count += count_left_leaves(root.right)
    return count
    pass

# Example tree:
#      A
#     / \
#    B   C
#   / \   \
#  D   E   F

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")

print(count_left_leaves(root)) # Expected output: 1