# signal 3
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-2, 3)

x = n

plt.stem(n, x)
plt.xlabel("n")
plt.ylabel("x[n]")
plt.title("Ramp Signal")
plt.grid(True)
plt.show()