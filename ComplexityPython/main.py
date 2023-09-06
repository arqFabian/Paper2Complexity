# Script for analyzing image complexity and  generate graphs

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from ComplexityAnalysis import calculate_complexity
from complexitygraph import generate_scatter_complexity

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

# create the scatter graph using the function for scatter graph
generate_scatter_complexity(file_names, complexity_scores, script_directory, 8)

