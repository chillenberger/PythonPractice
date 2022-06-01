# Hashing is useful for identifing the uniqueness of data.
# python has a build in funciton hash() to hash data.

import bisect

#Data Structures and Algorithms hash table exercises.
def ex_1(lst1, lst2): # brings in list of numbers.
    hash_table = {}
    for i in lst1:
        hash_table[i] = True
    rsp = [i for i in lst2 if hash_table.get(i)]
    return rsp

def ex_2 (string):
    hash_table = {}
    for i in string:
        if hash_table.get(i):
            hash_table[i] +=1
        else:
            hash_table[i] = 1
    for i in hash_table:
        if hash_table[i] > 1:
            return i
    return False

def ex_3(string):
    string.replace(' ', '')
    hash_table =  {i:True for i in string}
    for c in range(ord('z')-ord('a')):
        if not hash_table.get(chr(c+ord('a'))):
            return chr(c+ord('a'))
    return False

def ex_4(string):
    hash_table = {}
    for c in string:
        if hash_table.get(c):
            hash_table[c] += 1
        else:
            hash_table[c] = 1

    for i in hash_table:
        if hash_table[i] == 1:
            return i
    return False

#leetcode example 2
def twoSum(lst, target):
    hash_table = {}
    for i in range(len(lst)):
        if hash_table.get(lst[i]):
            hash_table[lst[i]].append(i)
        else:
            hash_table[lst[i]] = [i]
    print(hash_table)

    if hash_table.get(target // 2):
        if len(hash_table.get(target //2 )) >= 2:
            print(hash_table.get(target // 2))
            return [hash_table.get(target // 2)[0], hash_table.get(target // 2)[1]]
    if hash_table.get(target) and hash_table.get(0):
        return [hash_table[0][0], hash_table[target][0]]

    for val in hash_table:
        lst_idx = hash_table[val][0]
        print(lst_idx)
        if hash_table.get(target-val) and hash_table[target-val][0] != lst_idx:
            return [lst_idx, hash_table[target-val][0]]
    return False


# lst1 = [1,4,3,7,65,2]
# lst2 = [5,3,4,7]
# print(ex_1(lst1, lst2))
# print(ex_2("abcdce"))
# print(ex_3("the quick brown box jumps over a lazy dog"))
# print(ex_4("minimum"))

# print(twoSum([-10, -1, -18, -19], -19))

class tree_node:
    def __init__(self, hashKey=None):
        self.hashKey = hashKey
        self.left = None
        self.right = None

# sorted using binary array
# lookup O(1) complexity
# node search O(log n)
# print sorted O(n)
# insert O(log n)
# delet O(log n)
class sorted_hashB():
    def __init__(self, hashKey, data=None):
        self.dict = {hashKey:data}
        self.root = tree_node(hashKey)

    def insert(self, hash, data, node=None):
        if node == None:
            node = self.root
        if hash < node.hashKey and node.left is not None:
            self.insert(hash, data, node.left)
        elif hash > node.hashKey and node.right is not None:
            self.insert(hash, data, node.right)
        elif hash < node.hashKey and node.left is None:
            node.left = tree_node(hash)
            self.dict[hash] = data
        elif hash > node.hashKey and node.right is None:
            node.right = tree_node(hash)
            self.dict[hash] = data

    def remove(self):
        pass

    def get_val(self, hash):
        return self.dict.get(hash)

    def show(self, node=False):
        if node == False:
            node = self.root
        if node == None:
            return

        self.show(node.left)
        print(node.hashKey, self.dict[node.hashKey])
        self.show(node.right)

def run_sorted_hashB():
    tree = sorted_hashB('John', 45)
    tree.insert('Beth', 13)
    tree.insert('zander', 89)
    tree.insert('Ken', 59)
    tree.insert('Aron', 32)
    tree.insert('Aaron', 23)
    tree.show()
    print(tree.get_val('Ken'))

# sorted hastable with ordered array.
# maintain sorted array to output ordered hash table
# look up O(1)
# ordered out O(n)
# insert O(n) for insert to move array elements O(log n ) binary search to maintain ordre in array
#
class sorted_hashArray:
    def __init__(self, key, data):
        self.arr = [key]
        self.dict = {key: data}

    def insert(self, key, data):
        index = self.__binary_search(key)
        self.__put(index, key)
        self.dict[key] = data

    def get_val(self, key):
        return self.dict[key]

    def show(self):
        for i in self.arr:
            print(i, self.dict[i])

    def __put(self, index, key):
        self.arr.insert(index, key)

    def __binary_search(self, key):
        index = bisect.bisect(self.arr, key)
        return index

def run_array_hash():
    table = sorted_hashArray('John', 43)
    table.insert('Becca', 33)
    table.insert('Dan', 32)
    table.insert('Zander', 89)
    table.insert('Aaron', 28)
    table.show()
    print(table.get_val('Dan'))


class sorted_hashLinked_node:
    def __init__(self, hash, data=None):
        self.hash = hash
        self.data = data
        self.next =  None

# lookup O(1)
# search O(n)
# insert O(1)
# show O(n)
# space O(n)
class sorted_hashLinked:
    # each hash gets the address of next hash alphabeticly.
    def __init__(self, hash, data):
        self.root = sorted_hashLinked_node(hash, data)
        self.dict = {hash:self.root}

    # insert in order
    def insert(self, node = None, hash = None, data = None):
        new_node = sorted_hashLinked_node(hash, data)
        self.dict[hash] = data
        if not node:
            node = self.root
        if not hash:
            raise Exception('A hash is required')

        # get location to insert new node
        node, last = self.search(hash)
        # if node and list exist then new node goes in between
        if node and last:
            last.next = new_node
            new_node.next =  node
        # if last is none the we repalce linked list head.
        if node and not last:
            self.root = new_node
            new_node.next = node
        # if node is none we are at end on linked list so add to end
        if not node and last:
            last.next = new_node
            new_node.next = None

    def search(self, hash):
        last = self.root
        node = self.root.next
        # special case for on item in list
        if node is None:
            if hash < last.hash:
                return last, None
            else:
                return None, last
        # when more than one item in list search through list.
        while node:
            if hash < last.hash:
                return last, None
            if hash > last.hash and hash < node.hash:
                return node, last
            if hash > node.hash:
                last = node
                node = node.next
        return node, last


    def get_val(self, hash):
        return self.dict.get(hash)

    def show(self):
        node = self.root
        while node:
            print(node.hash, node.data)
            node = node.next

    def delete(self):
        pass

def run_sorted_hashedLinked():
    tree = sorted_hashLinked('John', 43)
    tree.insert(hash='Becca', data=33)
    tree.insert(hash="Dan", data=32)
    tree.insert(hash="Zander", data=14)
    tree.insert(hash='Aaron', data=28)
    tree.show()
    print(tree.get_val('Aaron'))
    node, last = tree.search('Chris')
    print(node.hash, last.hash)

# sorts on call to show uses quick sort method nlog(n) speed
# bad because if we wante to iterate through in order we would
# copy database so space 2*n or O(n)
# insert O(1)
# del O(1)
# search O(1)
class brute_force:
    def __init__(self, key, value):
        self.dict = {key: value}

    def insert(self, key, value):
        self.dict[key] = value

    def show(self):
        for i in sorted(self.dict):
            print(i)

    def get_val(self, key):
        return self.dict[key]

def run_brute_force():
    dict = brute_force('John', 43)
    dict.insert('Becca', 33)
    dict.insert('Dan', 32)
    dict.insert('Zander', 14)
    dict.insert('Aaron', 28)
    dict.show()
    print(dict.get_val('Aaron'))







def sorting_with_hash():
    pass

if __name__ == '__main__':
    # run_sorted_hashB()
    run_sorted_hashedLinked()
    # run_brute_force()
    # run_array_hash()
