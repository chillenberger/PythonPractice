import numpy as np


a = np.array([[5,2,3], [1,2, 5]])
b = np.array([[1,2,3], [1,2,3]])
av = a.view()

# print(id(a[1,1]), id(av[1,1]))
# print(id(a[1,1]) == id(av[1,1]))
# print(a[1,1] is av[1,1])


# print(a, av)
# av[1][1] = 100
# print(a, av)

c = np.concatenate([a,b])
print(a)
print(np.where(a==5, 0, -1))

arr = np.array([1.2,4.3,3.5,5,4,4])
c = np.subtract(a,b)
print(np.cumsum(arr))