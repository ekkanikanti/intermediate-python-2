import numpy as np

print('Random numbers: ')
nums = np.random.random_sample((10,))
print(nums)
# https://stackoverflow.com/questions/11873741/sampling-random-floats-on-a-range-in-numpy

print('Mean: ' + str(np.mean(nums)))
print('Median: ' + str(np.median(nums)))
print('Standard Deviation: ' + str(np.std(nums)))
# https://www.geeksforgeeks.org/python-statistics-median/