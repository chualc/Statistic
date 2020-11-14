# http://scipy.github.io/devdocs/generated/scipy.stats.linregress.html#scipy.stats.linregress

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Square Feet (X)
x = np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700])
# House Price in $1000s (Y)
y = np.array([245, 312, 279, 308, 199, 219, 405, 324, 319, 255])

# Perform the linear regression
res = stats.linregress(x, y)

# Coefficient of determination (R-squared)
print(f"R-squared: {res.rvalue**2:.6f}")

# Intercept and Slope
print(f"Intercept: {res.intercept}  Slope: {res.slope}")

# Plot the data along with the fitted line:
# https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html
original = plt.plot(x, y, 'o', label='original data')

plottedX = np.arange(0,3001,500)
plt.plot(plottedX, res.intercept + res.slope*plottedX, '--', label='plotted line')

fitted = plt.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')

plt.xlabel("Square Feet")
plt.ylabel("House Price ($1000s)")
plt.xlim(0, 3000)
plt.ylim(0, 450)
plt.show()
