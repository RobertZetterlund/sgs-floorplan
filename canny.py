import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from cv2 import cv2


from skimage import feature


# Generate noisy image of a square
#im = np.zeros((128, 128))
#im[32:-32, 32:-32] = 1
#
#im = ndi.rotate(im, 15, mode='constant')
#im = ndi.gaussian_filter(im, 4)
#im += 0.2 * np.random.random(im.shape)

im = cv2.imread("downloads/file1450.png")
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

print(np.shape(im))

# Compute the Canny filter for two values of sigma
edges1 = feature.canny(im)
edges2 = feature.canny(im, sigma=3)

# display results
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
                                    sharex=True, sharey=True)
cmap = plt.get_cmap("gray")

ax1.imshow(im, cmap=cmap)
ax1.axis('off')
ax1.set_title('noisy image', fontsize=20)

ax2.imshow(edges1, cmap=cmap)
ax2.axis('off')
ax2.set_title(r'Canny filter, $\sigma=1$', fontsize=20)

ax3.imshow(edges2, cmap=cmap)
ax3.axis('off')
ax3.set_title(r'Canny filter, $\sigma=3$', fontsize=20)

fig.tight_layout()

plt.show()