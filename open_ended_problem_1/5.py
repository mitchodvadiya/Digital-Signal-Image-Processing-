# signal 5
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5, 6)

x = np.zeros(len(n))

x[n == 0] = 1
x[n == 1] = 3
x[n == -1] = 5

plt.stem(n, x)
plt.xlabel("n")
plt.ylabel("x[n]")
plt.title("Impulse Signal")
plt.grid(True)
plt.show()