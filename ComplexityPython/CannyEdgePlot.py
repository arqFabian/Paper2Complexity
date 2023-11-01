import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os

# Working function for side by side comparison of Original and Edge detection image
def process_image1(image_path):
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
    plt.title('Edge detection Image'), plt.xticks([]), plt.yticks([])

    # Use tight_layout to ensure proper layout and fit legend
    plt.tight_layout()

    plt.show()


# Example usage:
# Get the directory of the script
script_directory = os.path.dirname(__file__)

# Define styles and extract the style names from folder names
input_folder = os.path.join(script_directory, 'input_images')
#filename = '1300.png' # Replace with the path to your image
#filename = '1959_SydneyOperaHouse.png'
filename = '1954_Notre-Dame-du-Haut-Ronchamp-France.jpg'
image_path = os.path.join(input_folder, filename)

process_image1(image_path)

input_folder = os.path.join(script_directory, 'render_images\Temp')
filename = '0010.png' # Replace with the path to your image
image_path = os.path.join(input_folder, filename)

process_image1(image_path)


# Working Plot of all edge detection Images

def process_images2(image_paths):
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
        img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

        # Check if the image was successfully read
        if img is None:
            raise Exception(f"File '{image_path}' could not be read. Please check if the file exists.")

        # Apply Canny edge detection
        edges = cv.Canny(img, 100, 200)

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
input_folder = os.path.join(script_directory, r'render_images\Temp')

# Create a list of image file paths in the input folder
image_paths = [os.path.join(input_folder, filename) for filename in os.listdir(input_folder) if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))]

# Process and display all images in a single plot window
process_images2(image_paths)





