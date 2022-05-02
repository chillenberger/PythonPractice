


# Data Structures and Algorithms
# pg 160 ex3
def numsum(low, high):
    if high == low:
        return low
    return high + numsum(low, high-1)


if __name__ == "__main__":
    print(numsum(0, 100))
