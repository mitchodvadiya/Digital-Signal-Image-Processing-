# Image 1 — Contrast Stretching
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Image_1.png", 0)

min_val = np.min(img)
max_val = np.max(img)

stretched = ((img - min_val) / (max_val - min_val) * 255).astype(np.uint8)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(stretched, cmap="gray")
plt.title("Contrast Stretching")
plt.axis("off")

plt.show()


# Image 2 — Histogram Equalization
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Image_2.png", 0)

equalized = cv2.equalizeHist(img)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(equalized, cmap="gray")
plt.title("Histogram Equalization")
plt.axis("off")

plt.show()


# Image 3 — Gamma Correction
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Image_3.png", 0)

gamma = 0.4

normalized = img / 255.0
gamma_img = np.power(normalized, gamma)
gamma_img = np.uint8(gamma_img * 255)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gamma_img, cmap="gray")
plt.title("Gamma Correction")
plt.axis("off")

plt.show()


# Image 4 — Gamma Correction
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Image_4.png", 0)

gamma = 0.3

normalized = img / 255.0
gamma_img = np.power(normalized, gamma)
gamma_img = np.uint8(gamma_img * 255)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gamma_img, cmap="gray")
plt.title("Gamma Correction")
plt.axis("off")

plt.show()


# Image 5 — Log Transformation
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Image_5.png", 0)

c = 255 / np.log(1 + np.max(img))

log_img = c * np.log(1 + img)
log_img = np.uint8(log_img)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(log_img, cmap="gray")
plt.title("Log Transformation")
plt.axis("off")

plt.show()