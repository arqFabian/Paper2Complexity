import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
import random

# Working function for side by side comparison of Original and Edge detection image
def process_image_edge_density(image_path):
    # Read the image from the specified file path
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image was successfully read
    if img is None:
        raise Exception("File could not be read. Please check if the file exists.")

    # Apply Canny edge detection
    edges = cv2.Canny(img, 100, 200)

    # Display the original and edge images
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge detection Image'), plt.xticks([]), plt.yticks([])

    # Use tight_layout to ensure proper layout and fit legend
    plt.tight_layout()

    plt.show()


# Working function for side by side comparison of Original and contour count image
def process_image_contours(image_path):

    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Check if the image was successfully read
    if image is None:
        raise Exception("File could not be read. Please check if the file exists.")

    # Apply Gaussian blur to reduce noise (optional)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edge image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a blank canvas of the same size as the image
    contour_image = np.zeros_like(image)

    # Define random BGR colors for contours
    colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in contours]

    # Draw each contour with a random color on the canvas
    for i, contour in enumerate(contours):
        cv2.drawContours(contour_image, [contour], -1, colors[i], 6)

    # Display the original and contour images with color map
    plt.subplot(121), plt.imshow(image, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(contour_image)
    plt.title('Contour count Image'), plt.xticks([]), plt.yticks([])


    """# Draw the contours on the canvas
    cv2.drawContours(contour_image, contours, -1, 255, 5)  # Draw all contours in white

    # Display the original and contour images
    plt.subplot(121), plt.imshow(image, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(contour_image, cmap='gray')
    plt.title('Contour Image'), plt.xticks([]), plt.yticks([])"""


    # Use tight_layout to ensure proper layout and fit legend
    plt.tight_layout()

    plt.show()


# Example usage:
# Get the directory of the script
script_directory = os.path.dirname(__file__)

# Define styles and extract the style names from folder names
input_folder = os.path.join(script_directory, 'input_images')
filename = '1954_Notre-Dame-du-Haut-Ronchamp-France.jpg'
image_path = os.path.join(input_folder, filename)

process_image_edge_density(image_path)
process_image_contours(image_path)

input_folder = os.path.join(script_directory, 'render_images')
filename = '0002.png' # Replace with the path to your image
image_path = os.path.join(input_folder, filename)

process_image_edge_density(image_path)
process_image_contours(image_path)

# Working Plot of all edge detection Images

def process_images_allimages_grid(image_paths):
    # Calculate the number of rows and columns for the grid
    num_images = len(image_paths)
    num_cols = 4  # You can change the number of columns as needed
    num_rows = (num_images + num_cols - 1) // num_cols

    # Create a figure with subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(12, 8))

    # Flatten the axes array for easy iteration
    axes = axes.flatten()

    for i, image_path in enumerate(image_paths):
        # Read the image from the specified file path
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Check if the image was successfully read
        if img is None:
            raise Exception(f"File '{image_path}' could not be read. Please check if the file exists.")

        # Apply Canny edge detection
        edges = cv2.Canny(img, 100, 200)

        """# Display the original image in the current subplot
        axes[i].imshow(img, cmap='gray')
        axes[i].set_title(f'Image {i+1}')
        axes[i].axis('off')  # Turn off axis labels"""

        # Display the edge detection image in the second subplot
        axes[i].imshow(edges, cmap='gray')
        axes[i].set_title(f'Edge Detection Lv {i+1}')
        axes[i].axis('off')  # Turn off axis labels

    # Use tight_layout to ensure proper layout
    plt.tight_layout()

    # Show the figure
    plt.show()


# Example usage:
# Get the directory of the script
script_directory = os.path.dirname(__file__)

# Define the folder containing images
input_folder = os.path.join(script_directory, r'render_images/Pattern1')

# Create a list of image file paths in the input folder
image_paths = [os.path.join(input_folder, filename) for filename in os.listdir(input_folder) if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))]

# Process and display all images in a single plot window
#process_images_allimages_grid(image_paths)







