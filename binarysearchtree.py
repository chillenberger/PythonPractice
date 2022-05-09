# A binary search tree is a tree where each node has at most to children
# lower value goes to left and higher child value goes to right.
# Binary trees have log(N) Search, Delete, and Insert time.

# used for generating unique data.
import random

class binary_search_tree:
    def __init__(self, root=None):
        self.root = root

    # Print out binary tree in an easy format
    # This is a depth first traversal, three types of DFS are pre-order,
    # in-order, post-order
    def show(self, node=False):
        if node is False:
            node = self.root
        if node is None:
            return
        # print(node.data) #pre-order traversal
        self.show(node.left)
        print(node.data) #in-order traversal
        self.show(node.right)
        # print(node.data) #post-order traversal

    # Find node with value we want
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

    # Insert new node to tree.
    def insert(self, new_node, node=None):
        # Start at root
        if node is None:
            node = self.root
        # If data already in tree return
        if node.data == new_node.data:
            return
        # Trickle throug tree until we find correct spot for data.
        if new_node.data < node.data and node.left is not None:
            self.insert(new_node, node.left)
        elif new_node.data > node.data and node.right is not None:
            self.insert(new_node, node.right)
        elif new_node.data < node.data and node.left is None:
            node.left = new_node
        elif new_node.data > node.data and node.right is None:
            node.right = new_node

    # Delete a node
    def delete(self, remove_data, node=False):
        # Start search for node to remove at root.
        if node is False:
            node = self.root
        # when the node is found, we return.
        if node is None:
            return None
        # Look at left and right child to find what direction down tree we go
        # Recursivly call delete on appropriate chld child
        # Set appropriate child to returned node, if data to remvoe < or >
        elif remove_data < node.data:
            node.left = self.delete(remove_data, node.left)
            return node
        elif remove_data > node.data:
            node.right = self.delete(remove_data, node.right)
            return node
        # If we found data to remove, evaluate its children
        elif remove_data == node.data:
            # If none or one child, shift tree up without worry
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # If two children, lift tree using lift method.
            else:
                node.right = self.lift(node.right, node)
                return node

    # Lifts tree for delete method
    def lift(self, node, node_to_delete):
        # search successive node, (smallest larger value)
        if node.left is not None:
            node.left = self.lift(node.left, node_to_delete)
            return node
        # When successive node found make copy data to node to delete
        else:
            node_to_delete.value = node.value
            return node.right

    # Return greatest number in tree.
    def greatest(self, node=False):
        if node is False:
            node = self.root
        if node.right is None:
            return node.data
        return self.greatest(node.right)


# Nodes to place into binary tree
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
