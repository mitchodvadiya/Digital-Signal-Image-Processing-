import numpy as np
import matplotlib.pyplot as plt

signal1 = np.array([1,2,3,4,5])
signal2 = np.array([2,4,6,8,10])

cross_corr = np.correlate(signal1, signal2, mode='full')
auto_corr = np.correlate(signal1, signal1, mode='full')

plt.figure(figsize=(8,8))

# Signal 1
plt.subplot(4,1,1)
plt.stem(signal1)
plt.title("signal1")
plt.xlabel("Time Lag")
plt.ylabel("Magnitude")

# Signal 2
plt.subplot(4,1,2)
plt.stem(signal2)
plt.title("signal2")
plt.xlabel("Time Lag")
plt.ylabel("Magnitude")

# Cross Correlation
plt.subplot(4,1,3)
plt.stem(cross_corr)
plt.title("Cross-correlation")
plt.xlabel("Time Lag")
plt.ylabel("Magnitude")

# Auto Correlation
plt.subplot(4,1,4)
plt.stem(auto_corr)
plt.title("Autocorrelation")
plt.xlabel("Time Lag")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()