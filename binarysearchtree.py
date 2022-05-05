# A binary search tree is a tree where each node has at most to children
# lower value goes to left and higher child value goes to right.
#

import random

class binary_search_tree:
    def __init__(self, root=None):
        self.root = root

    def show(self, node=False):
        if node is False:
            node = self.root
        if node is None:
            return
        self.show(node.left)
        print(node.data)
        self.show(node.right)

    def search(self, data, node=False):
        if node is False:
            node = self.root
        if node.data == data:
            return node
        elif node.left:
            self.search(data, node.left)
        elif node.right:
            self.search(data, node.right)
        return

    def insert(self, new_node, node=None):
        if node is None:
            node = self.root
        if node.data == new_node.data:
            return
        if new_node.data < node.data and node.left is not None:
            self.insert(new_node, node.left)
        elif new_node.data > node.data and node.right is not None:
            self.insert(new_node, node.right)
        elif new_node.data < node.data and node.left is None:
            node.left = new_node
        elif new_node.data > node.data and node.right is None:
            node.right = new_node

    def delete(self, remove_data, node=False):
        if node is False:
            node = self.root

        if node is None:
            return None
        elif remove_data < node.data:
            node.left = self.delete(remove_data, node.left)
            return node
        elif remove_data > node.data:
            node.right = self.delete(remove_data, node.right)
            return node
        elif remove_data == node.data:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.right = self.lift(node.right, node)
                return node

    def lift(self, node, node_to_delete):
        if node.left is not None:
            node.left = self.lift(node.left, node_to_delete)
            return node
        else:
            node_to_delete.value = node.value
            return node.right

    def greatest(self, node=False):
        if node is False:
            node = self.root
        if node.right is None:
            return node.data
        return self.greatest(node.right)



class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        left = str(self.left.data) if self.left else str(None)
        right = str(self.right.data) if self.right else str(None)
        return "data: "+ str(self.data) + \
                " left: "+ left+ \
                " right: "+ right

if __name__ == '__main__':
    min_rand = 0
    max_rand = 10000
    node1 = node(random.randint(min_rand, max_rand))

    tree = binary_search_tree(node1)

    nodes = []
    for i in range(1000):
        nodes.append(node(random.randint(min_rand, max_rand)))
        tree.insert(nodes[i])

    tree.show()
    node_add = node(random.randint(min_rand, max_rand))
    print(f"\nnode_add: {node_add}")
    tree.insert(node_add)
    print("\n")
    tree.show()
    tree.delete(node_add.data)
    print("\n")
    tree.show()

    print(tree.greatest())
