import matplotlib.pyplot as plt

test_scores = [55, 45, 88, 75, 43, 56, 89, 98, 55, 54, 65, 77, 88, 81, 82, 89, 92, 98, 65, 76, 76, 73, 72, 84]

x = [x for x in range(len(test_scores))]

plt.bar(x, test_scores)
plt.show()

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(test_scores, bins, histtype='bar', rwidth=0.8)
plt.show()

plt.hist(test_scores, bins, histtype='bar',cumulative=True, rwidth=0.8)
plt.show()
