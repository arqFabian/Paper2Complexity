import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def process_image(image_path):
    # Read the image from the specified file path
    img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

    # Check if the image was successfully read
    if img is None:
        raise Exception("File could not be read. Please check if the file exists.")

    # Apply Canny edge detection
    edges = cv.Canny(img, 100, 200)

    # Display the original and edge images
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

# Example usage:
image_path = '1500.jpg'  # Replace with the path to your image
process_image(image_path)