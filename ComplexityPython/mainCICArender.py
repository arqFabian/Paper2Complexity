# Script for analyzing image complexity and  generate graphs

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as mcolors
import os


from complexityanalysis import calculate_complexity
from complexitygraph import generate_scatter_render_complexity_together, generate_scatter_render_complexity_separate

# Get the directory of the script
script_directory = os.path.dirname(__file__)

# Define styles and extract the style names from folder names
input_folder = os.path.join(script_directory, 'render_images')
pattern_names = [folder for folder in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, folder))]

# Create a colormap for styles
style_cmap = plt.get_cmap('tab20')  # Change 'tab20' to the desired colormap name

# Initialize lists to store data
file_paths = []
complexity_scores = []
pattern_labels = []
levels = []

# Iterate through pattern folders and images
for pattern in pattern_names:
    style_path = os.path.join(input_folder, pattern)
    for filename in os.listdir(style_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            image_path = os.path.join(style_path, filename)
            complexity = calculate_complexity(image_path)
            level = int(filename.split('.')[0])  # Extract the name from the filename
            file_paths.append(image_path)
            complexity_scores.append(complexity)
            pattern_labels.append(pattern)
            levels.append(level)

# Print all results
for result in complexity_scores:
    print(result)

######################
#In process to include the contour count

"""# Initialize lists to store data
file_paths = []
complexity_scores = []
edge_score = []
contour_score = []
pattern_labels = []
levels = []

# Iterate through pattern folders and images
for pattern in pattern_names:
    style_path = os.path.join(input_folder, pattern)
    for filename in os.listdir(style_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            image_path = os.path.join(style_path, filename)
            edge_density, contour_count = calculate_complexity(image_path)
            edge_score.append(edge_density)
            contour_score.append(contour_count)
            level = int(filename.split('.')[0])  # Extract the name from the filename
            file_paths.append(image_path)
            complexity_scores.append(complexity)
            pattern_labels.append(pattern)
            levels.append(level)

# Print all results
for result in complexity_scores:
    print(result)"""

######################

# create the scatter graph using the function for scatter graph with all three patterns together
#generate_scatter_render_complexity_together(levels, complexity_scores, pattern_labels, pattern_names, script_directory, 1)

# create the scatter graph using the function for scatter graph with all three patterns together

generate_scatter_render_complexity_separate(levels, complexity_scores, pattern_labels, pattern_names, script_directory)
