import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Load Audio File
audio_file = "vidssave.com श्री राम स्तुति _ Shri Ram Chandra Kripalu Bhajman l  shorts  jaishreeram ram viral youtubeshorts LOW.mp3"
audio, sample_rate = sf.read(audio_file)

# Convert stereo to mono
if audio.ndim == 2:
    audio = np.mean(audio, axis=1)

print("Sample Rate :", sample_rate)
print("Total Samples :", len(audio))

# Normalize audio
audio = audio / np.max(np.abs(audio))

# Different Impulse Responses
impulse_responses = {
    "IR1": np.array([1.0, 0.5]),
    "IR2": np.array([1.0, -0.5]),
    "IR3": np.array([1.0, 0.0, 0.5]),
    "IR4": np.array([0.5, 1.0, 0.5])
}

# Processing
for name, h in impulse_responses.items():
    print(f"\nProcessing {name}")

    # Convolution
    convoluted = convolve(audio, h, mode='same')

    # Normalize
    convoluted = convoluted / np.max(np.abs(convoluted))

    # Approximate inverse filter
    inverse_filter = np.zeros(len(h))
    inverse_filter[0] = 1 / h[0]

    for i in range(1, len(h)):
        inverse_filter[i] = -h[i] / (h[0] ** 2)

    # Restore signal
    restored = convolve(convoluted, inverse_filter, mode='same')

    restored = restored / np.max(np.abs(restored))

    # Save audio files
    sf.write(f"{name}_Convolved.wav", convoluted, sample_rate)
    sf.write(f"{name}_Restored.wav", restored, sample_rate)

    # Plot
    plt.figure(figsize=(12,6))

    plt.subplot(3,1,1)
    plt.plot(audio[:5000])
    plt.title("Original Audio")

    plt.subplot(3,1,2)
    plt.plot(convoluted[:5000])
    plt.title(f"{name} - Convolved Audio")

    plt.subplot(3,1,3)
    plt.plot(restored[:5000])
    plt.title(f"{name} - Restored Audio (Inverse Filtering)")

    plt.tight_layout()
    plt.show()

print("\nProcessing Completed Successfully!")