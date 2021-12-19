import numpy as np
neta_arr=np.array(
        [[1,2],
        [10,12],
        [30,20]]
)
test_point = np.array([5,10])

subtract = neta_arr - test_point

squared_arr = subtract**2

summed_arr = squared_arr.sum(axis=1)

print(summed_arr)

print(summed_arr.argmin())

dictionary = {
    0: [[1,2],[3,4],[5,6]],
    1: [[1,2],[3,4],[5,6]]
}
dictionary[1]