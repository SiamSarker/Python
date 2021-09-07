import numpy as np
import matplotlib.pyplot as plt
import random
points = np.array([
    [1, 2],
    [2, 1],
    [3, 1],
    [5, 4],
    [5, 5],
    [6, 5],
    [10, 8],
    [7, 9],
    [11, 5],
    [14, 9],
    [14, 14],
    ])

print(points)
n = points.tolist()
print(n)

# print(points[:,0])
# x = points[:,0]
# y = points[:,1]
#
# plt.scatter(x, y, s=0.8, marker='*', label="inisial data" )
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Initial Data Points")
# plt.legend()
#
# plt.show()