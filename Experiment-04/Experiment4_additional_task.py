
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, bilinear, cheby1, lfilter

# Signal specifications
sampling_frequency = 20000
duration = 0.02
t = np.arange(0, duration, 1 / sampling_frequency)

# Generate four sine waves
x1 = np.sin(2 * np.pi * 1000 * t)
x2 = np.sin(2 * np.pi * 2000 * t)
x3 = np.sin(2 * np.pi * 3000 * t)
x4 = np.sin(2 * np.pi * 4000 * t)

# Plot all four signals
plt.figure(figsize=(10, 8))

for i, (signal, f) in enumerate(
    zip([x1, x2, x3, x4], [1000, 2000, 3000, 4000]), 1
):
    plt.subplot(4, 1, i)
    plt.plot(t, signal)
    plt.title(f'Sine Wave: {f} Hz')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

plt.tight_layout()
plt.show()


# Add all four signals
x = x1 + x2 + x3 + x4


# Function to plot time and frequency domains
def plot_signal(signal, title):
    # Time domain
    plt.figure(figsize=(10, 4))
    plt.plot(t, signal)
    plt.title(title + ' - Time Domain')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

    # Frequency domain
    N = len(signal)
    spectrum = np.fft.rfft(signal)
    frequency = np.fft.rfftfreq(
        N, d=1 / sampling_frequency
    )

    magnitude = np.abs(spectrum) * 2 / N
    magnitude[0] /= 2

    plt.figure(figsize=(10, 4))
    plt.stem(frequency, magnitude)
    plt.xlim(0, 6000)
    plt.title(title + ' - Frequency Domain')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()


# Plot combined signal
plot_signal(x, 'Combined Signal')


# Filter specifications
filter_order = 4
ripple = 0.5


# Butterworth filter with 2 kHz cutoff
cutoff_butter = 2000

# Prewarp cutoff for bilinear transformation
warped_butter = 2 * sampling_frequency * np.tan(
    np.pi * cutoff_butter / sampling_frequency
)

analog_b, analog_a = butter(
    filter_order,
    warped_butter,
    analog=True,
    btype='low'
)

digital_b, digital_a = bilinear(
    analog_b, analog_a, sampling_frequency
)

# Filter the combined signal
y_butter = lfilter(digital_b, digital_a, x)

# Plot Butterworth output
plot_signal(y_butter, 'Butterworth Output - 2 kHz Cutoff')


# Chebyshev Type-I filter with 3 kHz cutoff
cutoff_cheby = 3000

warped_cheby = 2 * sampling_frequency * np.tan(
    np.pi * cutoff_cheby / sampling_frequency
)

analog_b, analog_a = cheby1(
    filter_order,
    ripple,
    warped_cheby,
    analog=True,
    btype='low'
)

digital_b, digital_a = bilinear(
    analog_b, analog_a, sampling_frequency
)

# Filter the combined signal
y_cheby = lfilter(digital_b, digital_a, x)

# Plot Chebyshev output
plot_signal(y_cheby, 'Chebyshev Output - 3 kHz Cutoff')
