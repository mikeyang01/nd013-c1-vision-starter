import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 10)
print(x)
plt.hist(x, 100)
plt.show()