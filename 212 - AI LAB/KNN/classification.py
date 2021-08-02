import random

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

for V in Val_set:
    for T in Train_set:


