# Script for analyzing image complexity and  generate graphs

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as mcolors
import os
import pandas as pd

from complexityanalysis import calculate_complexity_score
from complexitygraph import generate_scatter_render_complexity_together, generate_scatter_render_complexity_separate
from complexitygraphcity import generate_scatter_city_complexity_together, generate_scatter_city_complexity_separate
# Get the directory of the script
script_directory = os.path.dirname(__file__)

# Define styles and extract the style names from folder names
input_folder = os.path.join(script_directory, 'city_images')
#input_folder = os.path.join(script_directory, 'example')
city_names = [folder for folder in os.listdir(input_folder) if os.path.isdir(os.path.join(input_folder, folder))]

# Create a colormap for styles
style_cmap = plt.get_cmap('tab20')  # Change 'tab20' to the desired colormap name

# Initialize lists to store data
file_paths = []
complexity_scores = []
city_labels = []
levels = []

#V1.0.1
# Working script for averaging results of CICA system for renders

# Iterate through city folders and images
for city in city_names:
    style_path = os.path.join(input_folder, city)

    # Dictionary to store complexity scores for each level
    level_complexity = {}

    for filename in os.listdir(style_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            image_path = os.path.join(style_path, filename)

            # Extract the level from the filename
            level = int(filename.split('_')[0])

            # Calculate complexity score for the image
            complexity = calculate_complexity_score(image_path)

            # Check for individual values (activate if needed)
            #print(complexity)
            # Append complexity score to the dictionary for the corresponding level
            if level in level_complexity:
                level_complexity[level].append(complexity)
            else:
                level_complexity[level] = [complexity]


    # Calculate the average complexity score for each level and append to lists
    for level, complexity_list in level_complexity.items():
        average_complexity = np.mean(complexity_list)
        file_paths.append(image_path)  # You can decide which image path to append here
        complexity_scores.append(average_complexity)
        city_labels.append(city)
        levels.append(level)

# Print all results
for result in complexity_scores:
    print(result)


# Create a DataFrame to store the data
data = {
    'City': city_labels,
    'Level': levels,
    'Image Scores': complexity_scores,
}

df = pd.DataFrame(data)

# Calculate average score per city
city_average = df.groupby('City')['Image Scores'].transform('mean')

# Add the city average to the DataFrame
df['City Average'] = city_average

# Print the DataFrame
print(df)


######################

# create the scatter graph using the function for scatter graph with all five cities together

generate_scatter_city_complexity_together(levels, complexity_scores, city_labels, city_names, script_directory, 5)
# create the scatter graph using the function for scatter graph with all five cities together

# generate_scatter_city_complexity_separate(levels, complexity_scores, city_labels, city_names, script_directory)
