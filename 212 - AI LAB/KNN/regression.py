import random
import math
import numpy as np

data_path = "/Users/siamsarker/Google Drive/Python/212 - AI LAB/KNN/Dataset/diabetes.csv"

print("Hello World")
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
    for j in range(length):
        dist = dist + pow((val1[j] - val2[j]), 2)
    return math.sqrt(dist)


Mean_Squared_Error = 0
K = 10                               # highest performance of K = 10 in validity set
error = 0

for testSet in Test_set:
    L = []
    for T in Train_set:
        dist = euclideanDistance(testSet, T, 10)
        L.append((T, dist))

    L.sort(key=lambda elem: elem[1])

    near = []
    for i in range(K):
        near.append(L[i][0])

    total = 0
    for i in range(len(near)):
        total = total + near[i][-1]
    avg = total / len(near)
    print(avg)

    error = error + math.sqrt(pow((testSet[-1] - avg), 2))


print("K is " + str(K))
print("Length of Test Set: " + str(len(Test_set)))
Mean_Squared_Error = error / float(len(Test_set))
print("Mean_Squared_Error : " + str(Mean_Squared_Error))