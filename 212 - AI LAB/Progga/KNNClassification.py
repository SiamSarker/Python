import math
import random
from collections import Counter
import numpy as np
from numpy import genfromtxt

datapath = '/Users/siamsarker/Google Drive/Python/212 - AI LAB/KNN/Dataset/iris.csv'
my_data = genfromtxt(datapath, delimiter=',')

# Dataset Prepare
data = my_data.tolist()
Train_set = []
Val_set = []
Test_set = []

random.shuffle(data)
# print(data)

for S in range(0, len(data)):
    R = random.uniform(0, 1)
    if R >= 0 and R <= 0.7:
        Train_set.append(data[S])
    elif R > 0.7 and R <= 0.85:
        Val_set.append(data[S])
    else:
        Test_set.append(data[S])

correct = 0
Val_acc = 0
K = 15

for V in Val_set:
    euclidean_distance = []  # distance calculation
    nearest_neighbour_list = []  # A list for nearest neighbour
    majority = []  # List for  majority class
    distance = []
    for T in Train_set:
        dis = math.sqrt(pow(V[0] - T[0], 2) + pow(V[1] - T[1], 2) + pow(V[2] - T[2], 2) + pow(V[3] - T[3], 2))
        euclidean_distance.append([dis, T[4]])
    euclidean_distance = sorted(euclidean_distance)

    for i in range(K):
        distance.append(euclidean_distance[i])  # add distance in distance
    nearest_neighbour_list = np.array(distance)  # reformat distance

    majority = (Counter(nearest_neighbour_list.flat)).most_common(1)  # count the quantity inside of an instance list

    if majority[0][0] == V[4]:  # check validation and majority train set
        correct += 1  # then increase correct one by one

# print(nearest_neighbour_list)
Val_acc = (correct / len(Val_set)) * 100  # Validation accuracy check
print(Val_acc)

correct = 0
Test_acc = 0
K = 15

for V in Test_set:
    euclidean_distance = []
    nearest_neighbour_list = []
    majority = []
    distance = []
    for T in Train_set:
        dis = math.sqrt(pow(V[0] - T[0], 2) + pow(V[1] - T[1], 2) + pow(V[2] - T[2], 2) + pow(V[3] - T[3], 2))
        euclidean_distance.append([dis, T[4]])
    euclidean_distance = sorted(euclidean_distance)

    for i in range(K):
        distance.append(euclidean_distance[i])
    nearest_neighbour_list = np.array(distance)

    majority = (Counter(nearest_neighbour_list.flat)).most_common(1)

    if majority[0][0] == V[4]:
        correct += 1  # suppose to be 1

# print(nearest_neighbour_list)
Test_acc = (correct / len(Test_set)) * 100
print(Test_acc)