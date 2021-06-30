import matplotlib.pyplot as plt
import numpy as np

lst = [-3, 4, -8, 9, 6, -7]
lst.sort(key=lambda x1: (x1 < 0, abs(x1)))

print(lst)

fig1 = plt.figure(num='fig111111', figsize=(10, 3), dpi=75, facecolor='#FFFFFF', edgecolor='#0000FF')
x = np.linspace(-1, 1, 5)
y = 2 * x + 1
path = plt.plot([1, 2, 3, 6], [4, 5, 8, 1], 'g.-')
fig2 = plt.figure(num='fig222222', figsize=(6, 3), dpi=75, facecolor='#FFFFFF', edgecolor='#FF0000')
plt.plot([5, 37, 32, 2])
# plt.savefig(path, dpi=300)
plt.show()
plt.close()
