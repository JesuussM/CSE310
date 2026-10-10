class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

""" Use a pointer to go through the whole linked list. At each node
    it looks at the data of the node to check against the target value.
    If the data and target match then it returns true, if it does not 
    then the pointer is set the the next node and checks again. It does
    this until the target is found or it reaches the end of the linked 
    list. When the node the pointer is looking at has None as next then 
    that is the last node."""
def find_value(head, target):
    pointer = head
    while pointer.next != None:
        if pointer.data == target:
            return True
        pointer = pointer.next
    return False

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

print(find_value(head, 30))
print(find_value(head, 50))