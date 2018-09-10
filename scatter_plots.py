import matplotlib.pyplot as plt

test_scores = [55, 45, 88, 75, 43, 56, 89, 98, 55, 54, 65, 77, 88, 81, 82, 89, 92, 98, 65, 76, 76, 73, 72, 84]
time_spent = [11, 10, 22, 23, 28, 32, 54, 55, 43, 23, 53, 33, 23, 55, 23, 33, 38, 48, 22, 35, 37, 42, 29, 12]

plt.scatter(time_spent, test_scores)
plt.title('Test scores vs Time Spent')
plt.xlabel('time spent on test')
plt.ylabel('Test Score')
plt.show()

x = [1, 2, 3, 4, 5]
y1 = [2, 3, 2, 4, 2]
y2 = [8, 8, 6, 7, 6]

plt.scatter(x, y1, marker='o', color='c')
plt.scatter(x, y2, marker='v', color='m')
plt.show()
