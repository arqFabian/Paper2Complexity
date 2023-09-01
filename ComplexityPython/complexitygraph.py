import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def generate_scatter_complexity(file_names_input, complexity_scores_input, script_directory_input, ):
    # Set the desired aspect ratio (16:9)
    aspect_ratio = 12 / 4

    # Calculate the figure width based on the aspect ratio
    fig_width = 8  # You can adjust this value as needed

    # Calculate the corresponding figure height
    fig_height = fig_width / aspect_ratio

    # Set the figure size with the desired aspect ratio
    plt.figure(figsize=(fig_width, fig_height))

    # Create a scatter plot with polynomial trend line
    plt.scatter(file_names_input, complexity_scores_input, marker='o', color='b')
    plt.xlabel('Chronological order of buildings')
    plt.ylabel('Complexity Score')
    plt.title('Facade Complexity Analysis')
    plt.grid(True)

    # Fit a polynomial trend line
    degree = 8 # Change this to the degree of the polynomial (e.g., 2 for quadratic)
    trend_coefficients = np.polyfit(file_names_input, complexity_scores_input, degree)
    trend_line = np.polyval(trend_coefficients, file_names_input)
    plt.plot(file_names_input, trend_line, color='r', linestyle='--', label='Trend Line')

    # Show the scatter plot with polynomial trend line
    plt.legend()

    # Specify the relative path to the Graphs directory from the script directory
    relative_graphs_path = os.path.join('..', 'src', 'Graphs')

    # Construct the full file path for saving the PDF
    save_path = os.path.join(script_directory_input, relative_graphs_path, 'complexitygraph.pdf')

    # Adjust figure margins to remove extra space
    plt.subplots_adjust(left=0.09, right=0.98, top=0.9, bottom=0.2)

    # Save the plot as a PDF file
    plt.savefig(save_path)
    plt.show()

    return
