import matplotlib.pyplot as plt
import csv
import numpy as np

x, y = np.loadtxt('example.txt', delimiter = ',', unpack = True)

plt.plot(x, y, label='Loaded from File')
plt.xlabel('Plot Number')
plt.ylabel('Randomly Chosen Tutorial #')
plt.legend()
plt.title('Awesome Graph')
plt.show()
