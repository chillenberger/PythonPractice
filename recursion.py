


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



if __name__ == "__main__":
    print(numsum(0, 100))

    dirty_lst = [1,2,[5, 4], [[],[[],4]],6,7,8]
    print_clean_lst(dirty_lst)
