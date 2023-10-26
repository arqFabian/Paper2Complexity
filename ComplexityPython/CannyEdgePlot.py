import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os

def process_image(image_path):
    # Read the image from the specified file path
    img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

    # Check if the image was successfully read
    if img is None:
        raise Exception("File could not be read. Please check if the file exists.")

    # Apply Canny edge detection
    edges = cv.Canny(img, 25, 200)

    # Display the original and edge images
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    # Use tight_layout to ensure proper layout and fit legend
    plt.tight_layout()

    plt.show()


# Example usage:
# Get the directory of the script
script_directory = os.path.dirname(__file__)

# Define styles and extract the style names from folder names
input_folder = os.path.join(script_directory, 'input_images')
filename = '1300.png' # Replace with the path to your image
image_path = os.path.join(input_folder, filename)

#process_image(image_path)

input_folder = os.path.join(script_directory, 'render_images\Pattern 1')
filename = '0001.png' # Replace with the path to your image
image_path = os.path.join(input_folder, filename)

process_image(image_path)