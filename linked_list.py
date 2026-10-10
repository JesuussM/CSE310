class Node:
      """Lightweight, nonpublic class for storing a singly linked node."""
      __slots__ = '_element', '_next'         # streamline memory usage
  
      def __init__(self, element, next):      # initialize node's fields
          self._element = element             # reference to user's element
          self._next = next                   # reference to next node

# 7.8.1
# Find second to last node
""" Use a pointer to go through the whole linked list. When the node
    the pointer is looking at has None as _next then that is the last
    node. So the node before it is the second to last."""
node1 = Node(1, None)
node2 = Node(2, None)
node3 = Node(3, None)
node4 = Node(4, None)
node5 = Node(5, None)

node1._next = node2
node2._next = node3
node3._next = node4
node4._next = node5

head = node1

index = head
while index._next != None:
    oldNode = index
    index = index._next
index = oldNode
print(index._element)

# 7.8.2
# Combine two singly linked list
"""After creating two signly linked list, we use a similar method to 
    find the last node. Then change the last node's _next to the head
    of the other singly linked list."""
Lnode1 = Node(1, None)
Lnode2 = Node(2, None)
Lnode3 = Node(3, None)
Lnode4 = Node(4, None)
Lnode5 = Node(5, None)
Lnode1._next = Lnode2
Lnode2._next = Lnode3
Lnode3._next = Lnode4
Lnode4._next = Lnode5
Lhead = Lnode1

Mnode1 = Node(6, None)
Mnode2 = Node(7, None)
Mnode3 = Node(8, None)
Mnode4 = Node(9, None)
Mnode5 = Node(10, None)
Mnode1._next = Mnode2
Mnode2._next = Mnode3
Mnode3._next = Mnode4
Mnode4._next = Mnode5
Mhead = Mnode1

lastNode = Lhead
while lastNode._next != None:
    lastNode = lastNode._next

lastNode._next = Mhead

# 7.8.3
# Find length of a singly linked list recurseively
"""Take in a head node as a parameter, if the node is None then it is 
    empty. Then call the function again but using its _next node.""" 
def get_size(head):
    if head is None:
        return 0
    return 1 + get_size(head._next)

print(get_size(Lhead))
