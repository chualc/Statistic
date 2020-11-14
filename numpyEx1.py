import numpy as np
from scipy import stats

dataset = [2000, 500, 300, 100, 100]

# mean
mean = np.mean(dataset)
print("Mean: ", mean)

# median
median = np.median(dataset)
print("Median: ", median)

# mode
mode = stats.mode(dataset)
print("Mode: ", mode)
