import math
import random
from collections import Counter
import numpy as np
from numpy import genfromtxt

file = open("DataSet/data.csv")
Data = np.loadtxt(file, delimiter=",")
file = open("DataSet/centers.csv")
Centers = np.loadtxt(file, delimiter=",")

print(Data)

print("Hi")
print(Centers)