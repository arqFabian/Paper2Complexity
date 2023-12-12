# Script for analyzing image complexity and  generate graphs

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as mcolors
import os


from complexityanalysis import calculate_complexity_score, calculate_metrics
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
edge_metric_scores = []
contour_metric_scores = []

# Initialize variables to keep track of maximum values
max_edge_metric = float('-inf')  # Initialize with negative infinity
max_contour_metric = float('-inf')  # Initialize with negative infinity

# Iterate through style folders and images
for style in style_names:
    style_path = os.path.join(input_folder, style)

    for filename in os.listdir(style_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            image_path = os.path.join(style_path, filename)

            # Calculate edge and contour metric scores for the image
            edges, contours = calculate_metrics(image_path)

            # Update maximum values if a new maximum is found
            max_edge_metric = max(max_edge_metric, edges)
            max_contour_metric = max(max_contour_metric, contours)

            # Extract the year from the filename
            year = int(filename.split('_')[0])

            # Append data to lists
            file_paths.append(image_path)
            edge_metric_scores.append(edges)
            contour_metric_scores.append(contours)
            style_labels.append(style)
            years.append(year)

            # Calculate complexity score for the image
            complexity = calculate_complexity_score(image_path)
            complexity_scores.append(complexity)

# Print the maximum values
print(f"Maximum Edge Metric Score: {max_edge_metric}")
print(f"Maximum Contour Metric Score: {max_contour_metric}")

# Print all complexity scores
#for result in complexity_scores:
    #print(result)

# create the scatter graph using the function for scatter graph
generate_scatter_complexity(years, complexity_scores, style_labels, style_names, script_directory, 9)



"""
# Iterate through style folders and images to find max metrics
for style in style_names:
    style_path = os.path.join(input_folder, style)

    for filename in os.listdir(style_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            image_path = os.path.join(style_path, filename)

            # Calculate edge and contour metric scores for the image
            edges, contours = calculate_metrics(image_path)

            # Update maximum values if a new maximum is found
            max_edge_metric = max(max_edge_metric, edges)
            max_contour_metric = max(max_contour_metric, contours)

            # Extract the year from the filename
            year = int(filename.split('_')[0])

            # Append data to lists
            file_paths.append(image_path)
            edge_metric_scores.append(edges)
            contour_metric_scores.append(contours)
            style_labels.append(style)
            years.append(year)

# Print the maximum values
print(f"Maximum Edge Metric Score: {max_edge_metric}")
print(f"Maximum Contour Metric Score: {max_contour_metric}")


# Calculate complexity scores
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
    print(result)"""



