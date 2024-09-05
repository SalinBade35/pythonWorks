import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Generate a list of angles for the circular shape
angles = np.linspace(0, 2 * np.pi, 100)

# Creating data for a circular shape
x = np.cos(angles)
y = np.sin(angles)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Plot the circle
ax.plot(x, y, color='black')

# Divide the circle into segments
segments = 12
for i in range(segments):
    start_angle = 2 * np.pi * i / segments
    end_angle = 2 * np.pi * (i + 1) / segments

    # Generate random RGB colors for each segment
    color = np.random.rand(3,)

    # Plot each segment as a filled region with an RGB color
    theta = np.linspace(start_angle, end_angle, 100)
    x_segment = np.cos(theta)
    y_segment = np.sin(theta)

    ax.fill_between(x_segment, y_segment, color=color)

# Load an image
image_path = 'your_image_path.jpg'  # Replace with your image file path
img = Image.open(image_path)
img = img.resize((100, 100))  # Resize image if needed

# Convert the image to a format that can be used by matplotlib
imgbox = OffsetImage(np.array(img), zoom=1)

# Create an annotation box with the image
ab = AnnotationBbox(imgbox, (0, 0), frameon=False, pad=0.5, xycoords='data', boxcoords="offset points")
ax.add_artist(ab)

# Remove the axes for aesthetic purposes
ax.set_axis_off()

# Set the aspect ratio to equal for a perfect circle
ax.set_aspect('equal')

# Display the plot
plt.show()
