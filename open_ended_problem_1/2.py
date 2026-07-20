# signal 2
import matplotlib.pyplot as plt

n = [0,1,2,3,4,5,6]
x = [1,2,3,3,2,1,0]

plt.step(n, x, where='post')
plt.scatter(n,x)
plt.grid(True)
plt.xlabel("n")
plt.ylabel("x[n]")
plt.title("Signal 2")
plt.show()