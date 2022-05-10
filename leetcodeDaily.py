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
