import functools

L1 = [1,2,3,4,5,6]
L2 = ['Real', 'Python']

def my_func(x):
    if x > 3: 
        return True 
    else: 
        return False

lam = lambda x: x>3

print(list(filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7])))
print(functools.reduce(lambda x, y: x*2+y, L1))
print(sum(x*2 for x in L1))
print((lambda x: (x + 3) * 5 / 2)(3))

lam2 = lambda x: ''.join(x)
print(lam2(L2))

