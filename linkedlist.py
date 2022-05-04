# linked lists are similar to arrays but arrays need contigious memory blocks
# and linked lists can have its memory spread throughout the computer.
# each node holds the address of the next node.  The first node is the head.
# the last node points to null. Python lists are not linked lists.
# linked lists are more efficient at inserting and deleting many items than lists
# due to not needing to shift all elements in list. for one element both have O(n)
# Can have doubly linked lists to traverse forward and backwords
# Circularly linked lists are possible.


# Linked list class
class linked_list:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.data)
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def left_append(self, node):
        node.next = self.head
        self.head = node

    def right_append(self, node):
        if self.head is None:
            self.head = node
        for n in self:
            pass
        n.next = node

    def find(self, val):
        if self.head is None:
            raise Exception("Empty List")
        for node in self:
            if node.data == val:
                return node
        raise Exception(f"value: {val} not found in list")

    def insert(self, new_node, idx):
        if self.head is None:
            raise Exception("Empty List")
        node = self.head
        for i in range(idx-1):
            node = node.next
        new_node.next = node.next
        node.next = new_node

    def delete_node(self, idx):
        if self.head is None:
            raise Exception("Empty List")
        if idx == 0:
            self.head = self.head.next

        for i, n in enumerate(self):
            if i == idx-1:
                n.next = n.next.next
                return
        raise Exception("Index out of range")

    def read(self, idx):
        if self.head is None:
            raise Exception("Empty List")
        for i, n in enumerate(self):
            if i == idx:
                return n
        raise Exception("Index out of range.")

    def reverse(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        last = None
        current = self.head
        while True:
            next = current.next
            current.next = last
            last = current
            current = next
            if next is None:
                break
        self.head = last




class ll_node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

if __name__ == '__main__':
    llist = linked_list()
    print(llist)

    node1 = ll_node('first')
    llist.left_append(node1)
    print(llist)

    node2 = ll_node('second')
    node1.next = node2
    print(llist)

    node3 = ll_node('new head')
    llist.left_append(node3)
    print(llist)

    node4 = ll_node('inserted')
    llist.insert(node4, 2)
    print(llist)

    node5 = ll_node('new_tail')
    llist.right_append(node5)
    print(llist)

    llist.delete_node(1)
    print(llist)

    llist.reverse()
    print(llist)
