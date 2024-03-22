# Script for analyzing image complexity and  generate graphs

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as mcolors
import os
import time

from complexityanalysis import calculate_complexity_score, calculate_metrics
from complexitygraph import generate_scatter_complexity

# Get the start time
start_time = time.time()

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

# Combine lists of complexity scores, file paths, and architectural styles
combined_data = list(zip(complexity_scores, file_paths, style_labels))

# Sort the combined data based on complexity scores
combined_data.sort(key=lambda x: x[0], reverse=True)  # Sort in descending order

# Extract top 5 high complexity scores with file names and architectural styles
top_5_high_complexity = combined_data[:5]

# Extract top 5 low complexity scores with file names and architectural styles
top_5_low_complexity = combined_data[-5:]

# Print the top 5 high complexity scores with file names and architectural styles
print("Top 5 High Complexity Scores:")
for score, file_path, style in top_5_high_complexity:
    file_name = os.path.basename(file_path)
    print(f"Image: {file_name}, Style: {style}, Complexity Score: {score}")

# Print the top 5 low complexity scores with file names and architectural styles
print("\nTop 5 Low Complexity Scores:")
for score, file_path, style in top_5_low_complexity:
    file_name = os.path.basename(file_path)
    print(f"Image: {file_name}, Style: {style}, Complexity Score: {score}")

# Print the maximum values
print(f"Maximum Edge Metric Score: {max_edge_metric}")
print(f"Maximum Contour Metric Score: {max_contour_metric}")
print(f"Total of Analyzed buildings:{len(complexity_scores)}")

# Print all complexity scores
#for result in complexity_scores:
    #print(result)

# Calculate the total processing time
end_time = time.time()
processing_time = end_time - start_time

# Print the processing time
print(f"Total processing time: {processing_time:.2f} seconds")

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



