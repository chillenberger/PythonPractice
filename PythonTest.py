import math

# completes the mtx making all rows the same length by filling space with 0's
def complete(mtx):
    longest_row = max([len(row) for row in mtx])
    for idx, row in enumerate(mtx):
        for i in range(longest_row-len(row)):
            mtx[idx].append(0)
    return mtx

# transpose matrix using nested loops.
def transpose_mtx(mtx):
    new = [[ mtx[col][row] for col in range(len(mtx[row]))] for row in range(len(mtx[0]))]
    return new

def transpose_mtx_map(mtx):
    new = map(list, zip(*mtx))
    return new

convert = {'I':1, 'V':5, 'X':10, 'L':'50', 'C':100, 'D':500, 'M':1000}
def romanNums(s):
    rsp = 0
    l = 0
    while l < len(s):
        if l+1<len(s) and s[l]+s[l+1] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
            rsp = rsp + convert[s[l+1]]-convert[s[l]]
            l += 2
        else:
            rsp = rsp + convert[s[l]]
            l += 1
        print(rsp)
    return rsp

# This code is contributed by Bhavya Jain


if __name__ == "__main__":
    print(romanNums("IIIVX"))
