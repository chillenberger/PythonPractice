
# Data Structures and Algorithms
# pg 160 ex3
def numsum(low, high):
    if high == low:
        return low
    return high + numsum(low, high-1)

# Data Structures and Algorithms
# pg 160 ex4
def print_clean_lst(lst):
    for i in lst:
        if isinstance(i, list):
            print_clean_lst(i)
        else:
            print(i)

# Data Structures and Algorithms
# practice to print string in reverse using recursion
def reverse_print(mystr):
    if len(mystr) == 0:
        return mystr
    rsp = mystr[-1]+reverse_print(mystr[0:-1])
    return rsp

# Data Structures and Algorithms
# practice recursion by counting x's in string
def count_xs(str):
    if not str:
        return 0
    if str[0] == "x":
        return 1 + count_xs(str[1:])
    else:
        return count_xs(str[1:])

# Data Structures and Algorithms
# staircase problem using recursion
def staircase(steps):
    if steps <= 0:
        return 0
    if steps == 1:
        return 1
    if steps == 2:
        return 2
    if steps == 3:
        return 4
    return staircase(steps-1) + staircase(steps-2) + staircase(steps-3)

# Data Structures and Algorithms
# anagram generator
def anagram_generator(str, anagrams = []):
    new_arry = []
    if len(str) == 1:
        return [str]
    anagrams = anagram_generator(str[1:], anagrams)
    for i in anagrams:
        for j in range(len(anagrams[0])):
            new_arry.append(i[0:j]+str[0]+i[j:])
        new_arry.append(i+str[0])
    return new_arry


# Data Structures and Algorithms
# pg 181 ex1
def count_lst_chr(lst):
    if not lst:
        return 0
    return len(lst[0]) + count_lst_chr(lst[1:])

# Data Structures and Algorithms
# pg 181 ex2
def return_even(lst):
    if not lst:
        return []
    if lst[0]%2 == 0:
        return [lst[0]] + return_even(lst[1:])
    else:
        return return_even(lst[1:])

# Data Structures and Algorithms
# pg 181 ex3
def triangular_num(num):
    if num == 0:
        return 0
    return num + triangular_num(num-1)

# Data Structures and Algorithms
# pg 182 ex4
def find_fist_x(str, idx=0):
    if idx == len(str):
        return
    if str[idx] == 'x':
        return idx
    else:
        return find_fist_x(str, idx+1)

# Data Structures and Algorithms
# pg 182 ex4
def shortest_path(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    return shortest_path(rows-1, cols) + shortest_path(rows, cols-1)

if __name__ == "__main__":
    print(numsum(0, 100))

    dirty_lst = [1,2,[5, 4], [[],[[],4]],6,7,8]
    print_clean_lst(dirty_lst)

    str = "hello"
    print(reverse_print(str))

    print(count_xs("abcxdxefx"))

    print(staircase(10))

    print(anagram_generator("abc"))

    print(count_lst_chr(['abc', 'rt', '', 'a']))

    print(return_even([1,2,3,4,5,6,7,8]))

    print(triangular_num(20))

    print(find_fist_x("abcdefghijklmnopqrstuvwxyz"))

    print(shortest_path(3, 3))
