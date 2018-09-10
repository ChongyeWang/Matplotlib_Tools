import matplotlib.pyplot as plt

x = [1, 2, 3 ,4, 5]
y = [4, 7, 4, 7, 3]

y2 = [5, 3, 2, 6, 2]

plt.plot(x, y, label="initial Line")
plt.plot(x, y2, label="New line!")
plt.xlabel('Plot Number')
plt.ylabel('random #')
plt.title('Epic Graph tutorial for data viz in Python with Matplotlib. \nTutorial showing labels and titles')
plt.legend()
plt.show()
