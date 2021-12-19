import numpy as np
import matplotlib.pyplot as plt

file = open("DataSet/data.csv")
Data = np.genfromtxt(file, delimiter=",")
file = open("DataSet/centers.csv")
Centers = np.genfromtxt(file, delimiter=",")

Clusters = [[], [], [], [], [], []]
Temp_Clusters = [[], [], [], [], [], []]

iteration = 0

while True:
    for S in Data:
        dist = []
        for C in Centers:
            dist.append((S[0]-C[0]) ** 2 + (S[1]-C[1]) ** 2)
        i = np.argmin(dist)
        Temp_Clusters[i].append(S.tolist())

    for i in range(len(Temp_Clusters)):
        Centers[i] = np.array(Temp_Clusters[i]).mean(axis=0)

    iteration = iteration + 1
    if iteration > 1:
        Shift = 0
        for S in Data:
            a = S[0]
            b = S[1]

            for i in range(len(Temp_Clusters)):
                for j in range(len(Temp_Clusters[i])):
                    if a == Temp_Clusters[i][j][0] and b == Temp_Clusters[i][j][1]:
                        c = i
            for i in range(len(Clusters)):
                for j in range(len(Clusters[i])):
                    if a == Clusters[i][j][0] and b == Clusters[i][j][1]:
                        d = i
            if c != d:
                Shift = Shift + 1
        print(Shift)
        if Shift < 10:
            Clusters = Temp_Clusters
            break
    Clusters = Temp_Clusters
    Temp_Clusters = [[], [], [], [], [], []]

for i in range(len(Clusters)):
    x = np.array(Clusters[i])[:, 0]
    y = np.array(Clusters[i])[:, 1]
    plt.scatter(x, y, s=0.8)

cx = Centers[:, 0]
cy = Centers[:, 1]
plt.scatter(cx, cy, color="r", marker='^', label="Center Point")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Data Points")
plt.legend()

plt.show()
