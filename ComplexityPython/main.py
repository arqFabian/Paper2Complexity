# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ComplexityAnalysis import calculate_complexity

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
plt.show()


