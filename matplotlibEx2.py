import matplotlib.pyplot as plt

# setup values
VALUES = [200, 300, 150, 250]
LABELS = ['Q1 2020', 'Q2 2020', 'Q3 2020', 'Q4 2020']

# draw a bar chart
plt.bar(LABELS, VALUES)
plt.ylabel("Revenue")

plt.show()