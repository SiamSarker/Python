import numpy as np
import matplotlib.pyplot as plt
import random
S = np.array([
    [1, 2],
    [3, 4]
    ])


C = [ [[1,2], [3,0] ] ]
TC = [ [ [3,0], [1,2] ] ]


try:
    print(TC[0].index(S[0].tolist()))
    print(C[0].index(S[0].tolist()))

except:
    pass









test = [[],[]]

test[0].append([2,3])
test[0].append([1,6])
test[1].append([4,5])
# print(test)

# print(points)
# n = points.tolist()
# print(n)

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