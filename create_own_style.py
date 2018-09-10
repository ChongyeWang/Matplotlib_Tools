import matplotlib.pyplot as plt
from matplotlib import style
import random


#Create our own style
style.use('ourstyle')


print(plt.__file__)
for label in range(8):
    x = []
    y = []

    for i in range(1, 10):
        ys = random.randrange(0, 15)
        xs = i
        x.append(xs)
        y.append(ys)

    plt.plot(x, y, label = label)

plt.legend()
plt.show()
