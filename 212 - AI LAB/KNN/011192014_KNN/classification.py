import random
import math
import operator
import numpy as np

data_path = "/Users/siamsarker/Google Drive/Python/212 - AI LAB/KNN/Dataset/iris.csv"
my_data = np.genfromtxt(data_path, delimiter=',')

data = my_data.tolist()

Train_set = []
Val_set = []
Test_set = []
random.shuffle(data)

for d in data:
    r = random.uniform(0, 1)
    if 0 <= r <= 0.7:
        Train_set.append(d)
    elif 0.7 < r <= 0.85:
        Val_set.append(d)
    else:
        Test_set.append(d)


def euclideanDistance(val1, val2, length):
    dist = 0
    for i in range(length):
        dist = dist + pow((val1[i] - val2[i]), 2)
    return math.sqrt(dist)


right = 0
accuracy = 0
K = 7                 # highest performance of K = 7 in validity set

for testSet in Test_set:
    L = []
    for T in Train_set:
        dist = euclideanDistance(testSet, T, 3)
        L.append((T, dist))

    L.sort(key=lambda elem: elem[1])

    near = []
    for i in range(K):
        near.append(L[i][0])

    counts = {}
    for i in range(len(near)):
        IClass = near[i][-1]
        if IClass in counts:
            counts[IClass] = counts[IClass] + 1
        else:
            counts[IClass] = 1

    sorted_d = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)

    nearestClass = sorted_d[0][0]

    if testSet[-1] == nearestClass:
        right = right + 1

print("K is " + str(K))
print("Length of Test Set: " + str(len(Test_set)))
print("Right : " + str(right))
accuracy = (right / float(len(Test_set))) * 100
print("Accuracy : " + str(accuracy) + "%")
