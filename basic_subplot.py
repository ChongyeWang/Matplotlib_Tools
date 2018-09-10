import random
import matplotlib.pyplot as plt

fig = plt.figure()

def create_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(8)
        xs.append(x)
        ys.append(y)

    return xs, ys

ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(325)
ax4 = fig.add_subplot(326)

x, y = create_plots()
ax1.plot(x, y)

x, y = create_plots()
ax2.plot(x, y)

x, y = create_plots()
ax3.plot(x, y)

x, y = create_plots()
ax4.plot(x, y)

plt.show()
