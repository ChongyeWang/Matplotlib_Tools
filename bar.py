import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
x2 = [1, 3, 5, 7, 9]

y = [4, 7, 4, 7, 3]
y2 = [5, 3, 2, 6, 2]

plt.bar(x, y, label="One", color='m')
plt.bar(x2, y2, label="Two", color='g')

plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('Bar Chart Tutorial')

plt.legend()
plt.show()
