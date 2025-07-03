# Enable interactive mode for the notebook
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('dat/einstein.png')
# Convert the image from BGR to RGB
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Convert the image to grayscale
image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
image = image / 255.0  

image = image[:200, 100:300]

# Downsample the image to improve performance
scale_percent = 100  # percent of original size

width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
image_small = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Scale the Z-axis values to make the image look flatter
z_scale = 1.7
image_scaled = image_small * 1/z_scale

# 3D plot the image based on pixel intensity
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
x, y = np.indices(image_small.shape)
ax.plot_surface(x, y, image_scaled, rstride=2, cstride=2, cmap='grey', edgecolor='none')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Pixel Intensity')
ax.set_zlim(0, z_scale)  # Set Z-axis limits
ax.set_title('3D Surface Plot of Image Pixel Intensities')

plt.rcParams['figure.dpi'] = 1000
print("3D Surface Plot of Image Pixel Intensities")
plt.show()