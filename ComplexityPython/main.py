# Script for analyzing image complexity and  generate graphs

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as mcolors
import os


from complexityanalysis import calculate_complexity
from complexitygraph import generate_scatter_complexity

# Get the directory of the script
script_directory = os.path.dirname(__file__)

# Define styles and extract the style names from folder names
input_folder = os.path.join(script_directory, 'input_images')
style_names = [folder for folder in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, folder))]

# Create a colormap for styles
style_cmap = plt.get_cmap('tab20')  # Change 'tab20' to the desired colormap name

# Initialize lists to store data
file_paths = []
complexity_scores = []
style_labels = []
years = []

# Iterate through style folders and images
for style in style_names:
    style_path = os.path.join(input_folder, style)
    for filename in os.listdir(style_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            image_path = os.path.join(style_path, filename)
            complexity = calculate_complexity(image_path)
            year = int(filename.split('_')[0])  # Extract the year from the filename
            file_paths.append(image_path)
            complexity_scores.append(complexity)
            style_labels.append(style)
            years.append(year)

# Print all results
for result in complexity_scores:
    print(result)

# create the scatter graph using the function for scatter graph
generate_scatter_complexity(years, complexity_scores, style_labels, style_names, script_directory, 9)

