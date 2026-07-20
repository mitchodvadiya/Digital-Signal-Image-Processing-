# signal 4
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-2, 12)

def u(n):
    return np.where(n >= 0, 1, 0)

x = u(n) - u(n-3) - 5*u(n-7)

plt.stem(n, x)
plt.xlabel("n")
plt.ylabel("x[n]")
plt.title("Unit Step Signal")
plt.grid(True)
plt.show()