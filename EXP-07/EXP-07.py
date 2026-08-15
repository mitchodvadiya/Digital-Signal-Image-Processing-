import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Image.jpg")

# Check whether image was loaded
if image is None:
    print("Error: Could not read the image.")
    exit()

# Display Original Image
plt.figure(figsize=(6, 6))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")
plt.show()

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display Grayscale Image
plt.figure(figsize=(6, 6))
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()