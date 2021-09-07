import numpy as np

supporters = [
    [1, 2],
    [4, 5],
    [10, 12]
]

supporters_nparray = np.array(supporters) #2d numpy array

new_neta_coordinate = supporters_nparray.mean(axis=0) #axis 0 means column


print(new_neta_coordinate)