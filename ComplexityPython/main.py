# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import numpy as np
import os

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from ComplexityAnalysis import calculate_complexity

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