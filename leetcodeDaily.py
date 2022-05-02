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
