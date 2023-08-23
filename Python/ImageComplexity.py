import cv2
import numpy as np
import os

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

"""%image_path = 'C:/Users/arqfa/Downloads/test2.png'  # Replace with the actual PNG image path
complexity_score = calculate_complexity(image_path)

print("Complexity Score:", complexity_score)"""

input_folder = 'C:/Users/arqfa/Downloads/complexity'  # Replace with the folder path
output_folder = 'C:/Users/arqfa/Downloads/complexity'  # Replace with the folder where you want to save results

# Iterate through all images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        image_path = os.path.join(input_folder, filename)
        complexity_score = calculate_complexity(image_path)

        # Create a result string
        result_string = f"{filename} complexity score: {complexity_score}"

        # Print the result
        print(result_string)

        # Save the result to a text file in the output folder
        result_file_path = os.path.join(output_folder, f"{filename.split('.')[0]}_result.txt")
        with open(result_file_path, 'w') as result_file:
            result_file.write(result_string)
