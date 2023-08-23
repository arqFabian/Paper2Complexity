import cv2
import numpy as np


def calculate_complexity(image_path, threshold_low=100, threshold_high=200):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian blur to reduce noise (optional)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, threshold_low, threshold_high)

    # Calculate complexity score based on edge density
    edge_density = np.count_nonzero(edges) / (edges.shape[0] * edges.shape[1])

    return edge_density
