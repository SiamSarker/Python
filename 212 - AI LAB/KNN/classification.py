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

# k - Hyperparameter turing

def euclideanDistance(val1, val2, length):
    dist = 0
    for i in range(length):
        dist = dist + pow((val1[i] - val2[i]), 2)
    return math.sqrt(dist)


right = 0
accuracy = 0
K = 3

for V in Val_set:
    L = []
    for T in Train_set:
        dist = euclideanDistance(V, T, 3)    # suppose to be N-1
        L.append((T, dist))
    # for i in range(5):
    #     print(distances[i])
    # print("")

    L.sort(key=lambda elem: elem[1])

    # for i in range(5):
    #     print(distances[i])
    # print("")
    # print("")
    # print("L  suppose to be huge")
    near = []

    # print(L)
    for i in range(K):
        near.append(L[i][0])

    # print("3 near list")
    # print(near)
    # print(len(near))
    # print("end")

    counts = {}
    for i in range(len(near)):
        IClass = near[i][-1]
        if IClass in counts:
            counts[IClass] = counts[IClass] + 1
        else:
            counts[IClass] = 1

    # print(counts)
    sorted_d = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
    # print(sorted_d)
    # print(sorted_d[0][0])

    nearestClass = sorted_d[0][0]

    if V[-1] == nearestClass:
        right = right + 1
    # print(V[-1])
    # print("Is it right?")
    # print(right)
    #
    #
    #
    #
    # print(V)
    #
    #
    #
    # print("")
    # print("")

print("K is "+str(K))
print("Length of Validaty Set: "+str(len(Val_set)))
print("Right : "+str(right))
accuracy = (right/float(len(Val_set))) * 100
print("Accuracy : "+str(accuracy) +"%")



