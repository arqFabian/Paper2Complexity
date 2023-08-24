# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from ComplexityAnalysis import calculate_complexity

# Get the directory of the script
script_directory = os.path.dirname(__file__)

# Construct the input folder path using the project folder as root

input_folder = os.path.join(script_directory, 'input_images')# Replace with the folder path
output_folder = os.path.join(script_directory, 'input_images') # Replace with the folder where you want to save results

# Initialize a list to store results
results = []

# Iterate through all images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        image_path = os.path.join(input_folder, filename)
        complexity_score = calculate_complexity(image_path)

        # Create a result string
        result_string = f"{filename} complexity score: {complexity_score}"

        # Add the result to the results list
        results.append(result_string)

# Print all results
for result in results:
    print(result)
