import matplotlib.pyplot as plt

HousePrice = [245, 312, 279, 308, 199, 219, 405, 324, 319, 255]
SquareFeet = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]

plt.scatter(SquareFeet, HousePrice)
plt.xlabel("Square Feet")
plt.ylabel("House Price")

plt.show()