import matplotlib.pyplot as plt
fig, (ax1, ax2)  =plt.subplots(2,1)
x = [1, 2, 3, 4, 5, 6, 7]
y = [5, 12, 19, 21, 31, 27, 35]
z = [3, 5, 11, 20, 15, 29, 31]

ax1.set_title('x y')
ax1.plot(x, y) 

ax2.set_title('x z')
ax2.plot(x, z)


fig.subplots_adjust(hspace=0.5)
plt.show()

