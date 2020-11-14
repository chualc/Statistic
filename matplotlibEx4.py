import matplotlib.pyplot as plt

barY = [100, 200, 180, 150]
lineY = [0, 20, 50, 100]
xLabel = ["Q1 2020", "Q2 2020", "Q3 2020", "Q4 2020"]

plt.bar(xLabel, barY)
plt.ylabel("Sales")

# create a different Y axis
plt.twinx()
plt.plot(xLabel, lineY, "o-", color="yellow")
plt.ylabel("Revenue")

plt.show()