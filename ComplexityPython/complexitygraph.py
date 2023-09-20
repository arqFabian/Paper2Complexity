import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle


def generate_scatter_complexity(years_input, complexity_scores_input, style_labels_input, style_names_input, script_directory_input, trendline_input):
    # Set the desired aspect ratio (16:9)
    aspect_ratio = 12 / 4

    # Calculate the figure width based on the aspect ratio
    fig_width = 12  # You can adjust this value as needed

    # Calculate the corresponding figure height
    fig_height = fig_width / aspect_ratio

    # Create a colormap for styles
    style_cmap = plt.get_cmap('tab20')  # Change 'tab20' to the desired colormap name

    # Assign colors based on style from the colormap
    style_colors = {style: style_cmap(i) for i, style in enumerate(style_names_input)}

    # Map the colors to the style labels
    point_colors = [style_colors[style] for style in style_labels_input]

    # Create a scatter plot
    # Set the figure size with the desired aspect ratio
    plt.figure(figsize=(fig_width, fig_height))
    plt.scatter(years_input, complexity_scores_input, c=point_colors, label=style_labels_input) # Add label to create legend

    # Set the legend to the right of the graph
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=style_colors[style], markersize=10, label=style) for
        style in style_names_input]

    # Add the trendline to the legend with a label
    handles.append(plt.Line2D([0], [0], color='r', linestyle='--', label='Trend Line'))

    plt.legend(handles=handles, title='Styles', loc='center left', bbox_to_anchor=(1, 0.5))  # Position legend to the right

    #label axis
    plt.xlabel('Chronological order of buildings')
    plt.ylabel('Complexity Score')
    plt.title('Facade Complexity Analysis by Year and Style')
    plt.grid(True)

    # Fit a polynomial trend line

    trend_coefficients = np.polyfit(years_input, complexity_scores_input, trendline_input) # Change this to the degree of the polynomial (e.g., 2 for quadratic)
    trend_line = np.polyval(trend_coefficients, years_input)
    plt.plot(years_input, trend_line, color='r', linestyle='--')

    # Use tight_layout to ensure proper layout and fit legend
    plt.tight_layout()

    # Specify the relative path to the Graphs directory from the script directory
    relative_graphs_path = os.path.join('..', 'src', 'Graphs')

    # Construct the full file path for saving the PDF
    save_path = os.path.join(script_directory_input, relative_graphs_path, 'complexitygraph.pdf')

    # Adjust figure margins to remove extra space
    #plt.subplots_adjust(left=0.09, right=0.98, top=0.9, bottom=0.2)

    # Save the plot as a PDF file
    plt.savefig(save_path, bbox_inches='tight')
    plt.show()

    return

