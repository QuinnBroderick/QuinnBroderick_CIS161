import numpy as np
array = np.random.randint(0,9, size=(5,5), dtype=int)
print (array)
print(array[1][2])
def sum_of_array(array):
    result = 0
    for row in array:
        for col in row:
            result += col
    return result
print(sum_of_array(array))
print(np.mean(array, axis=1))
print(np.max(array, axis=1))
