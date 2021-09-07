import math
import random
import statistics
from numpy import genfromtxt

datapath = '/Users/siamsarker/Google Drive/Python/212 - AI LAB/KNN/Dataset/diabetes.csv'
my_data = genfromtxt(datapath, delimiter=',')

# Data Prepare
data = my_data.tolist()
Train_set = []
Val_set = []
Test_set = []

random.shuffle(data)
# print(data)

for S in range(0, len(data)):
    R = random.uniform(0.0, 1.0)
    if R >= 0 and R <= 0.7:
        Train_set.append(data[S])
    elif R > 0.7 and R <= 0.85:
        Val_set.append(data[S])
    else:
        Test_set.append(data[S])


# Distance calculate
def euclidean_distance(V, T):
    distance = 0.0

    for i in range(len(V) - 1):
        distance += pow((V[i] - T[i]), 2)
        # print(distance)
    return math.sqrt(distance)


# Error Calculate
def Error_Calculation(sample, average):
    error = 0
    for i in range(len(sample)):
        if sample[i] != average:
            error = error + (sample[i] - average)
    Mean_Squared_Error = math.sqrt(error / float(len(sample)))
    return Mean_Squared_Error


# Mean_Squared_Error for Validation set
k = 15
distance = []
d = list()
for V in range(len(Val_set)):
    for T in range(len(Train_set)):
        distance.append(euclidean_distance(Val_set[V], Train_set[T]))
distance.sort()

for i in range(k):
    print(i, "distance: ", distance[i])

Avg = statistics.mean(distance)
print(Avg)

Mean_Squared_Error_Val = Error_Calculation(Val_set[V], Avg)
print("Mean Squared Error for Validation set: ", Mean_Squared_Error_Val)

# Mean_Squared_Error for Test set
k = 5
distances = []
d = list()
for V in range(len(Test_set)):
    for T in range(len(Train_set)):
        distances.append(euclidean_distance(Test_set[V], Train_set[T]))
distances.sort()

for i in range(k):
    print(i, "distance: ", distances[i])

Average = statistics.mean(distances)

Mean_Squared_Error_test = Error_Calculation(Test_set[V], Average)
print("Mean Squared Error for Test set: ", Mean_Squared_Error_test)