# linked lists are similar to arrays but arrays need contigious memory blocks
# and linked lists can have its memory spread throughout the computer.
# each node holds the address of the next node.  The first node is the head.
# the last node pooints to null. Python lists are not linked lists.


# Linked list class
class linked_list:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

class ll_node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


if __name__ == "__main__":
    llist = linked_list()
    node1 = ll_node('first')
    llist.head = node1
    node2 = ll_node('second')
    node1.next = node2
    print(llist)
    for i in llist:
        print(i)
