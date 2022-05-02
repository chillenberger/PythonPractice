# Hashing is useful for identifing the uniqueness of data.
# python has a build in funciton hash() to hash data.

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

print(twoSum([-10, -1, -18, -19], -19))
