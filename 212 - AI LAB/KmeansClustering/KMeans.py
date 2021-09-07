import math
import random
from collections import Counter
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

file = open("DataSet/data.csv")
Data = np.genfromtxt(file, delimiter=",")
file = open("DataSet/centers.csv")
Centers = np.genfromtxt(file, delimiter=",")

# Clusters = [[]]
# Temp_Clusters = [[]]

iteration = 0

# def euclideanDistance(val1, val2):
#     return math.sqrt(pow((val1 - val2), 2))
#
# while True:
#     for S in Data:
#         for C in Centers:




print(Data[:, 0])

x = Data[:, 0]
y = Data[:, 1]
plt.scatter(x, y, s=1.2, marker='*', label="Data Point")

cx = Centers[:, 0]
cy = Centers[:, 1]
plt.scatter(cx, cy, color="r", marker='^', label="Center Point")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Initial Data Points")
plt.legend()

plt.show()
