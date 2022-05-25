# leetcode 399, 4/30/22
# Evaluate division
def calcEquation( equations, values, queries):
    result = {} #hash table of values
    independent_eqs = [] # trackes independent sets of equaitons

    set_index = 0 # index of independent equations
    for eq in equations:
        if not result.get(eq[0]) and not result.get(eq[1]): # if no value for a or b we found new set
            result[eq[0]] = 1   # set a to 1
            independent_eqs.append(set()) # make space for new set
            set_index += 1
        for i, equ in enumerate(equations):
            a, b = equ
            if result.get(a) and not result.get(b):
                result[b] = result[a]/values[i]
                independent_eqs[set_index-1].update({a, b})
            elif result.get(b) and not result.get(a):
                result[a] = result[b]*values[i]
                independent_eqs[set_index-1].update({a, b})

    rsp = []
    for a,b in queries:
        same_set = False
        for equ_set in independent_eqs:
            if a in equ_set and b in equ_set:
                same_set = True
                break
        if same_set and result.get(a) and result.get(b):
            rsp.append(result.get(a)/result.get(b))
        else:
            rsp.append(-1)

    return rsp


# leetcode daily 5/9/2022
# Given a string containing digits from 2-9 inclusive, return all possible letter
# combinations that the number could represent. Return the answer in any order.
class Solution5_9_2022:
    dct = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
            '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
            '8':['t','u','v'], '9':['w','x','y','z']}

    def letterCombinations(self, digits: str) -> list[str]:
        # if empty input return empty list
        if len(digits) == 0 or len(digits) > 4:
            return []
        # convert string to lst to delete first character
        digits_s = [x for x in digits]
        # container to save new values
        new_values = []
        # dequeue first digit from list
        current = digits_s[0]
        del digits_s[0]
        # if last digit return its value
        if len(digits_s) == 0:
            new_values = []
            for c in Solution.dct[current]:
                new_values.append(c)
            return new_values

        # continue to call untill all digits dequed from input digits
        old_values = self.letterCombinations(''.join(digits_s))
        # perform all combinations and append to a new list
        for c in old_values:
            for d in Solution.dct[current]:
                new_values.append(d+c)
        # return new list
        return new_values


# leetcode daily, 5/10/2022
# 216. Combination Sum III
# find k intagers that sum to n
# solution uses backtracking
class Solution5_10_22:
    def __init__(self):
        self.ans = []

    def solve(self, a, pos, k, n):
        if pos == k:
            if sum(a) == n:
                self.ans.append(a[:])
        for i in range(a[-1]+1 if a else 1,10):
            a.append(i)
            self.solve(a, pos+1, k, n)
            a.pop()


    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        if n > 45:
            return
        a = []
        self.solve(a, 0, k, n)
        return self.ans
# run
# test = Solution5_10_22()
# print(test.combinationSum3(9, 45))


# leetcode
# 3. Longest Substring Without Repeating Characters
# used sliding window technique
def lengthOfLongestSub(s):
    longest = 0
    for i in range(len(s)):
        j = i
        while j < len(s):
            repeat = s[j] in s[i:j]
            if repeat:
                longest = j-i if j-i>longest else longest
                break
            elif j+1 == len(s) and not repeat:
                longest = j-i+1 if j-i+1 > longest else longest
                break

            j += 1

    return longest

#leetcode
# 14. Longest Common Prefix
# time O(n*m) where m is shortest string n is len of strs
# space O(m) size of common
def longestCommonPrefix(strs):
    # variable to hold common prefix
    common = ''
    str_len = 0
    # iterate through characters in first str in list
    for i in range(len(strs[0])):
        # verify char is in every str in list
        for j in strs:
            str_len = len(j)
            # if we exceed len of shortest str return common
            if len(j) == i:
                return common
            # if not return common
            if strs[0][i] != j[i]:
                return common
        # if not returned we append new valuue to common
        common += strs[0][i]
    # if iterate through entire str then it is the common prefix.
    return common
#run
# lst = ['ab', 'abc', 'abce']
# print(longestCommonPrefix(lst))

# leetcode
# 4. Median of Two Sorted Arrays
# Algorithm reference https://www.youtube.com/watch?v=LPFhl65R7ww
class Solution_4:
    max_neg = -1000
    max_pos = 1000

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # find initial x and y arr positions
        x_arr, y_arr = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        x_end = len(x_arr)-1
        y_end = len(y_arr)-1
        x_start = 0
        x_pos = (x_end+x_start)//2
        y_pos = (len(x_arr)+len(y_arr)+1)//2-x_pos

        i=0 # testing
        # Edge Case: len x = 1
        # if len(x) == 1:
        #     if not (len(x)+len(y))%2:
        #         return min(y_arr[y_pos-1, x_arr[0]])


        while x_pos <= len(x_arr) or x_pos >= 0:
            # hold x and y values for comparison
            print(f"x_pos: {x_pos}, y_pos: {y_pos}")
            xH = x_arr[x_pos] if x_pos < len(x_arr) else Solution_4.max_pos
            xL = x_arr[x_pos-1] if x_pos > 0 else Solution_4.max_neg
            yH = y_arr[y_pos]
            yL = y_arr[y_pos-1]
            print(f"xL: {xL} xH: {xH}, yL: {yL}, yH: {yH}")

            # found median so return
            if xL <= yH and yL <= xH:
                return (float(max(xL, yL)) if not (len(x_arr)+len(y_arr))%2
                    else (max(xL, yL)+min(xH, yH))/2)
            # x_arr median is too high so move left
            elif xL >= yH:
                x_end = x_pos-1
                x_pos = (x_end+x_start)//2
                y_pos = (len(x_arr)+len(y_arr)+1)//2-x_pos
                # Edge case: if x_pos is < 0 then min x_arr is greater than
                # max y_arr so get median and return
                if x_pos < 0:
                    x_pos = 0
                    xL = x_arr[0]
                    y_pos = (len(x_arr)+len(y_arr)+1)//2-x_pos
                    yL = y_arr[y_pos]
                    yH = y_arr[y_pos+1]
                    if not (len(x_arr)+len(y_arr))%2:
                        return (y_arr[yL]+max(y_arr[yH], x_arr[xL]))/2
                    else:
                        return yL
            # x_arr median is too low so move right
            else:
                x_start = x_pos+1
                x_pos = (x_end+x_start)//2
                y_pos = (len(x_arr)+len(y_arr)+1)//2-x_pos
                # Edge case:
                # x_pos is > length of x_arr then all x_arr is less than y_arr
                if x_pos > len(x_arr):
                    x_pos = len(x_arr)-1
                    xH = x_arr[-1]
                    y_pos = (len(x_arr)+len(y_arr)+1)//2-x_pos
                    yL = y_arr[y_pos]
                    yH = y_arr[y_pox+1]
                    if not (len(x_arr)+len(y_arr))%2:
                        return (min(yL, xH)+yH)/2
                    else:
                        return yL
            i+=1
            if i > 10:
                return False

def check(arr1, arr2):
    arr1.extend(arr2)
    arr1.sort()
    print(arr1)
    if not len(arr1)%2:
        print((arr1[len(arr1)//2]+arr1[len(arr1)//2-1])/2)
    else:
        print(arr1[len(arr1)//2])
# run
# test = Solution_4()
# arr1 = [1,3, 8, 9, 15]
# arr2 = [7, 11, 18, 19, 21, 25]
# print(test.findMedianSortedArrays( arr1, arr2 ))
# check(arr1, arr2)

# leetcode
# 21. Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getMinNode(node1, node2):
    if node1 > node2:
        return 2, node2
    else:
        return 1, node1

def mergeTwoLists(list1, list2):

    if not list1 and not list2:
        return None

    rsp_head = ListNode()
    rsp = rsp_head

    current1 = list1
    current2 = list2

    while current1 is not None or current2 is not None:
        # get lowest value
        if current1 is not None and current2 is None:
            idx, val = 1, current1.val
        elif current1 is None and current2 is not None:
            idx, val = 2, current2.val
        else:
            idx, val = getMinNode(current1.val, current2.val)

        # incriment linked list lowest value found in
        if idx == 2:
            current2 = current2.next
        else:
            current1 = current1.next

        rsp.val = val
        # if nothing left in linked lists break loop to not attach new node.
        if current1 is None and current2 is None:
            rsp.next = None
            break

        # if something in linked lists add a node and continue
        rsp.next = ListNode()
        rsp = rsp.next

    return rsp_head
# run
# first1 = ListNode(1)
# first1.next = ListNode(3)
# first1.next.next = ListNode(5)
#
# second1 = ListNode(2)
# second1.next = ListNode(3)
# second1.next.next = ListNode(4)
# out = mergeTwoLists(ListNode(None), ListNode(None))
# while out is not None:
#     print(out.val)
#     out = out.next

# leetcode
# 20. Valid Parentheses
def isValid(s):
    table = {')':'(', '}':'{', ']':'['}
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
        elif stack[-1] == table.get(c):
            stack.pop()
        else:
            stack.append(c)
    return True if not stack else False

# run
# print(isValid('(){}[]'))


# LeetCode
# 28. Implement strStr()
def strStr(haystack, needle):
    print(needle)
    if not needle:
        return 0
    c = 0
    while c < len(haystack):
        for i in range(len(needle)):
            # if needle runs off end of haystack or needle not in haystack next
            print(c+i, len(haystack))
            if c > len(haystack)-1 or haystack[c] != needle[i]:
                c -= i
                break
            # if i == len needle then we know needle is in haystack return start pos
            elif i == len(needle)-1:
                return c-i
            # increment
            else:
                c += 1
        c += 1
    return -1

# 28. Implement strStr() but using python build in methods.
def strStr2(haystack, needle):
    return 0 if not needle else haystack.find(needle)
# run
# print(strStr("missippi", "issi"))
# print(strStr2("missippi", "issi"))

# leetcode
# 9. Palindrome Number
# memory O(n) n = len number
# time O(n) n = len number
def isPalindrome(number):
    num = [x for x in str(number)]
    while len(num) > 1:
        if num[0] == num[-1]:
            num.pop()
            del num[0]
        else:
            return False
    return True

# memory O(1)
# time O(n) n = len number
def isPalindrome2(number):
    num = str(number)
    while len(num) > 1:
        if num[0] == num[-1]:
            num = num[1:-1]
        else:
            return False
    return True
# run
print(isPalindrome2(123321))
