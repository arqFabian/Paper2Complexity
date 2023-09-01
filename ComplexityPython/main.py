# Script for analyzing image complexity and  generate graphs

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from ComplexityAnalysis import calculate_complexity
from complexitygraph import scattergraphcomplexity

# Get the directory of the script
script_directory = os.path.dirname(__file__)

# Construct the input folder path using the project folder as root

input_folder = os.path.join(script_directory, 'input_images')# Replace with the folder path
output_folder = os.path.join(script_directory, 'input_images') # Replace with the folder where you want to save results

# Initialize lists to store file names and complexity scores
file_names = []
complexity_scores = []

# Iterate through all images in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg")):
        """if filename.endswith(".png"):"""
        image_path = os.path.join(input_folder, filename)
        complexity_score = calculate_complexity(image_path)

        # Append file name (number) and complexity score to lists
        file_names.append(int(filename.split('.')[0]))
        complexity_scores.append(complexity_score)

# Print all results
for result in complexity_scores:
    print(result)

# create the scatter graph
scattergraphcomplexity(script_directory, file_names, complexity_scores)

"""# Set the desired aspect ratio (16:9)
aspect_ratio = 12 / 4

# Calculate the figure width based on the aspect ratio
fig_width = 8  # You can adjust this value as needed

# Calculate the corresponding figure height
fig_height = fig_width / aspect_ratio

# Set the figure size with the desired aspect ratio
plt.figure(figsize=(fig_width, fig_height))

# Create a scatter plot with polynomial trend line
plt.scatter(file_names, complexity_scores, marker='o', color='b')
plt.xlabel('Image Number')
plt.ylabel('Complexity Score')
plt.title('Image Complexity Analysis')
plt.grid(True)

# Fit a polynomial trend line
degree = 8  # Change this to the degree of the polynomial (e.g., 2 for quadratic)
trend_coefficients = np.polyfit(file_names, complexity_scores, degree)
trend_line = np.polyval(trend_coefficients, file_names)
plt.plot(file_names, trend_line, color='r', linestyle='--', label='Trend Line')

# Show the scatter plot with polynomial trend line
plt.legend()

# Specify the relative path to the Graphs directory from the script directory
relative_graphs_path = os.path.join('..', 'src', 'Graphs')

# Construct the full file path for saving the PDF
save_path = os.path.join(script_directory, relative_graphs_path, 'complexitygraph.pdf')

# Adjust figure margins to remove extra space
plt.subplots_adjust(left=0.09, right=0.98, top=0.9, bottom=0.2)

# Save the plot as a PDF file
plt.savefig(save_path)
plt.show()"""

