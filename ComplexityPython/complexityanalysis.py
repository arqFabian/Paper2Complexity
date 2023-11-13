import cv2
import numpy as np


def calculate_complexity1(image_path, threshold_low=50, threshold_high=150):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian blur to reduce noise (optional)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, threshold_low, threshold_high)

    # Calculate input_images score based on edge density
    edge_density = np.count_nonzero(edges) / (edges.shape[0] * edges.shape[1])

    return edge_density


def calculate_complexity(image_path, threshold_low=50, threshold_high=150):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian blur to reduce noise (optional)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, threshold_low, threshold_high)

    # Find contours in the edge image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate input_images score based on edge density and contour count
    edge_density = np.count_nonzero(edges) / (edges.shape[0] * edges.shape[1])

    # Normalize edge density to be in the range [0, 1]
    edge_density_normalized = (edge_density - 0) / (.0255 - 0) # 0.0255 adjusted from 255

    contour_count = len(contours)
        # ======
        # 0.0255 (255 is max possible value for an 8-bit grayscale image) because the value was so small I adjusted it to 0.0255 but this value should be reviewed
        # ======

    # Normalize contour count to be in the range [0, 1]
    max_contour_count = 6000  # Adjust this value based on your data
    contour_count_normalized = contour_count / max_contour_count

        # There is a value of 5000 among the data however this value should be adjusted based on max value in contour count for the correct normalization before proceding with the calculation

    # Combine edge density and contour count with weights
    weight_edge_density = 0.6
    weight_contour_count = 0.4

    complexity_score = (
            weight_edge_density * edge_density_normalized +
            weight_contour_count * contour_count_normalized
    )

    return complexity_score


#In process to integrate automized contour count and edge density normalization
"""
def calculate_complexity(image_path, threshold_low=50, threshold_high=150):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian blur to reduce noise (optional)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, threshold_low, threshold_high)

    # Find contours in the edge image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate edge density and contour count
    edge_density = np.count_nonzero(edges) / (edges.shape[0] * edges.shape[1])
    contour_count = len(contours)

    return edge_density, contour_count


def calculate_complexity_score(edge_density, contour_count, weight_edge_density=0.8, weight_contour_count=0.2, max_contour_count=100):
    # Normalize edge density and contour count
    edge_density_normalized = edge_density / 255.0  # Normalize edge density to [0, 1]
    contour_count_normalized = contour_count / max_contour_count  # Normalize contour count to [0, 1]

    # Calculate complexity score
    complexity_score = (
        weight_edge_density * edge_density_normalized +
        weight_contour_count * contour_count_normalized
    )

    return complexity_score


def find_max_contour_count(image_paths):
    max_count = 0

    for image_path in image_paths:
        _, contour_count = calculate_complexity(image_path)
        max_count = max(max_count, contour_count)

    return max_count"""