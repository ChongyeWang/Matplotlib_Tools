import matplotlib.pyplot as plt

labels = 'Taxes', 'Overhead', 'Entertainment'

sizes = [25, 32, 12]
colors = ['c', 'm', 'b']

plt.pie(sizes, labels=labels, colors=colors, startangle=90, shadow = True, explode = (0.1, 0.1, 0.1), autopct = '%1.1f%%')
plt.axis('equal')
plt.show()
