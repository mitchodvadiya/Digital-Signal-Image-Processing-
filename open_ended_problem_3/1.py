import librosa
import numpy as np
import matplotlib.pyplot as plt

# Load Audio Files

original, sr1 = librosa.load("ed-sheeran-shape-of-you-official-music-video_JiWtRXIL.mp3", sr=22050)
karaoke, sr2 = librosa.load("ed-sheeran-shape-of-you-karaoke-version_OG6u0UNZ.mp3", sr=22050)
different, sr3 = librosa.load("with-you-ap-dhillon-official-music-video_pTZD0ZjA.mp3", sr=22050)

print("Original Shape :", original.shape)
print("Karaoke Shape :", karaoke.shape)
print("Different Shape :", different.shape)

print("Sample Rates :", sr1, sr2, sr3)

# Make Same Length

min_len = min(len(original), len(karaoke), len(different))

original = original[:min_len]
karaoke = karaoke[:min_len]
different = different[:min_len]

# Normalize

original = (original - np.mean(original)) / np.std(original)
karaoke = (karaoke - np.mean(karaoke)) / np.std(karaoke)
different = (different - np.mean(different)) / np.std(different)

# Extract MFCC Features

mfcc_original = librosa.feature.mfcc(y=original, sr=sr1, n_mfcc=13)
mfcc_karaoke = librosa.feature.mfcc(y=karaoke, sr=sr2, n_mfcc=13)
mfcc_different = librosa.feature.mfcc(y=different, sr=sr3, n_mfcc=13)

# Average MFCCs

mfcc_original_mean = np.mean(mfcc_original, axis=1)
mfcc_karaoke_mean = np.mean(mfcc_karaoke, axis=1)
mfcc_different_mean = np.mean(mfcc_different, axis=1)

# Correlation

corr_ok = np.corrcoef(mfcc_original_mean, mfcc_karaoke_mean)[0,1]
corr_od = np.corrcoef(mfcc_original_mean, mfcc_different_mean)[0,1]
corr_kd = np.corrcoef(mfcc_karaoke_mean, mfcc_different_mean)[0,1]

print("\nCorrelation Results")
print("Original vs Karaoke  :", corr_ok)
print("Original vs Different:", corr_od)
print("Karaoke vs Different :", corr_kd)

# Plot MFCC Features

plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.plot(mfcc_original_mean, marker='o')
plt.title("Original Song MFCC")

plt.subplot(3,1,2)
plt.plot(mfcc_karaoke_mean, marker='o')
plt.title("Karaoke Song MFCC")

plt.subplot(3,1,3)
plt.plot(mfcc_different_mean, marker='o')
plt.title("Different Song MFCC")

plt.tight_layout()
plt.show()

# Correlation Bar Graph

labels = [
    "Original\nvs\nKaraoke",
    "Original\nvs\nDifferent",
    "Karaoke\nvs\nDifferent"
]

values = [corr_ok, corr_od, corr_kd]

plt.figure(figsize=(6,4))
plt.bar(labels, values)

plt.ylabel("Correlation")
plt.title("Audio Track Similarity")

for i, value in enumerate(values):
    plt.text(i, value, f"{value:.2f}", ha="center", va="bottom")

plt.show()