# A trie is a tree build from hash table.  each node is a hash table pointing to the
# address of another hash table.  This is commonly used for word auto complete.



class trie:
    def __init__(self):
        self.root = node()

    # search for a word in the trie, return last node found
    def search(self, word):
        current_node = self.root
        # check every character in string to determin if in trie
        for chr in word:
            if current_node.children.get(chr):
                current_node = current_node.children[chr]
            # if not in return
            else:
                return
        # return final node
        return current_node

    # insert a word into trie
    def insert(self, word):
        # start at root
        current_node = self.root
        # check every character in word
        for chr in word:
            # if character already in trie move on
            if current_node.children.get(chr):
                current_node = current_node.children[chr]
            # else add new characters by appending nodes.
            else:
                new_node = node()
                current_node.children[chr] = new_node
                current_node = current_node.children[chr]
        current_node.children["*"] = None

    # shows all word starting with a specific char, for testing.
    def show_dict(self, node=None, word="", words=[]):
        # start at beginning if no node passed in
        current_node = node or self.root
        # itterate through all nodes in each node
        for key, childNode in current_node.children.items():
            # if at end node, meaning full word, append word to words list.
            if key == "*":
                words.append(word)
            # else add character to word and pass to next recurrsion.
            else:
                self.show_dict(childNode, word+key, words)
        # return word list.
        return words

class node:
    def __init__(self):
        self.children = {}


if __name__ == "__main__":
    my_trie = trie()
    my_trie.insert("hello")
    my_trie.insert("hell")
    my_trie.insert("climbing")
    my_trie.insert("quickdraw")
    print(my_trie.show_dict())
