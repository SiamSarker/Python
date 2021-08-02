import random
import math
import numpy as np

data_path = "/Users/siamsarker/Google Drive/Python/212 - AI LAB/KNN/Dataset/iris.csv"
my_data = np.genfromtxt(data_path, delimiter=',')

data = my_data.tolist()

Train_set = []
Val_set = []
Test_set = []
random.shuffle(data)

type(data)

for d in data:
    r = random.uniform(0, 1)
    if 0 <= r <= 0.7:
        Train_set.append(d)
    elif 0.7 < r <= 0.85:
        Val_set.append(d)
    else:
        Test_set.append(d)

# k - Hyperparameter turing
K = 5

def euclideanDistance(val1, val2, length):
    dist = 0
    for i in range(length):
        dist = dist + pow((val1[i] - val2[i]), 2)
    return math.sqrt(dist)

for V in Val_set:
    distances = []
    for T in Train_set:
        dist = euclideanDistance(V, T, 3)    # suppose to be N-1
        distances.append((T, dist))
    # for i in range(5):
    #     print(distances[i])
    # print("")

    distances.sort(key=lambda elem: elem[1])

    # for i in range(5):
    #     print(distances[i])
    # print("")
    # print("")
    near = []
    K = 5
    print(distances)
    for i in range(K):
        near.append(distances[i][0])

    print(near)

    counts = {}
    for i in range(len(near)):
        IClass = near[i][-1]
        if IClass in counts:
            counts[IClass] = counts[IClass] + 1
        else:
            counts[IClass] = 1

    print(near)
    print("")
    # counts.sort(key=lambda elem: elem[1], reverse= True)  #sort
    print(near)

    print("")
    print("")











