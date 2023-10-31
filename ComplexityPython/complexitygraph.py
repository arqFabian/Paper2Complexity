import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from itertools import cycle


def generate_scatter_complexity(years_input, complexity_scores_input, style_labels_input, style_names_input, script_directory_input, trendline_input):
    # Set the desired aspect ratio (16:9)
    aspect_ratio = 12 / 4

    # Calculate the figure width based on the aspect ratio
    fig_width = 12  # You can adjust this value as needed

    # Calculate the corresponding figure height
    fig_height = fig_width / aspect_ratio

    # Create a colormap for styles
    color_ref = ['prism', 'tab20', 'tab20b', 'tab20c', 'Set3']
    # Define the colormap reference directly
    selected_colormap = color_ref[3]
    style_cmap = plt.get_cmap(selected_colormap)  # Change 'tab20' to the desired colormap name

    # Assign colors based on style from the colormap
    style_colors = {style: style_cmap(i) for i, style in enumerate(style_names_input)}

    # Map the colors to the style labels
    point_colors = [style_colors[style] for style in style_labels_input]

    # Create a scatter plot
    # Set the figure size with the desired aspect ratio
    plt.figure(figsize=(fig_width, fig_height))
    plt.scatter(years_input, complexity_scores_input, c=point_colors,
                label=style_labels_input)  # Add label to create legend

    # Set the legend to the right of the graph
    handles = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=style_colors[style], markersize=10, label=style) for
        style in style_names_input]

    # Add the trendline to the legend with a label
    handles.append(plt.Line2D([0], [0], color='r', linestyle='--', label='Trend Line'))

    plt.legend(handles=handles, title='Styles', loc='center left',
               bbox_to_anchor=(1, 0.5))  # Position legend to the right

    # label axis
    plt.xlabel('Chronological order of buildings')
    plt.ylabel('Complexity Score')
    plt.title('Facade Complexity Analysis by Year and Style')
    plt.grid(True)

    # Fit a polynomial trend line

    trend_coefficients = np.polyfit(years_input, complexity_scores_input, trendline_input)
    # Change @trendline_input@  to the degree of the polynomial (e.g., 2 for quadratic)
    trend_line = np.polyval(trend_coefficients, years_input)
    plt.plot(years_input, trend_line, color='r', linestyle='--')

    # Use tight_layout to ensure proper layout and fit legend
    plt.tight_layout()

    # Specify the relative path to the Graphs directory from the script directory
    relative_graphs_path = os.path.join('..', 'src', 'Graphs')

    # Construct the full file path for saving the PDF
    save_path = os.path.join(script_directory_input, relative_graphs_path, 'complexitygraph.pdf')

    # Adjust figure margins to remove extra space
    # plt.subplots_adjust(left=0.09, right=0.98, top=0.9, bottom=0.2)

    # Save the plot as a PDF file
    plt.savefig(save_path, bbox_inches='tight')
    plt.show()

    return


# This function plots all three patterns in a single scatter graph
def generate_scatter_render_complexity_together(level_input, complexity_scores_input, pattern_labels_input, pattern_names_input, script_directory_input, trendline_input):
    # Create a colormap for patterns
    color_ref = ['prism', 'tab20', 'tab20b', 'tab20c', 'Set3', 'Set1']
    style_cmap = plt.get_cmap(color_ref[5])  # Change 'tab20' to the desired colormap name

    # Initialize a list to store the unique patterns and their corresponding indices
    unique_patterns = []
    pattern_indices = []

    # Identify unique patterns and their indices
    for pattern in pattern_labels_input:
        if pattern not in unique_patterns:
            unique_patterns.append(pattern)
        pattern_indices.append(unique_patterns.index(pattern))

    # Set the desired aspect ratio (16:9)
    aspect_ratio = 12 / 4

    # Calculate the figure width based on the aspect ratio
    fig_width = 12  # You can adjust this value as needed

    # Calculate the corresponding figure height
    fig_height = fig_width / aspect_ratio

    # Set up the figure
    plt.figure(figsize=(fig_width, fig_height))

    # Plot points and lines for each pattern
    for i, pattern in enumerate(unique_patterns):
        pattern_indices_i = [j for j, index in enumerate(pattern_indices) if index == i]
        plt.scatter([level_input[j] for j in pattern_indices_i],
                    [complexity_scores_input[j] for j in pattern_indices_i],
                    color=style_cmap(i), label=pattern, marker='o', s=50)

        # Fit a polynomial trend line for each pattern
        trend_coefficients = np.polyfit([level_input[j] for j in pattern_indices_i],
                                        [complexity_scores_input[j] for j in pattern_indices_i], trendline_input)
        trend_line = np.polyval(trend_coefficients, [level_input[j] for j in pattern_indices_i])
        plt.plot([level_input[j] for j in pattern_indices_i], trend_line, color=style_cmap(i), linestyle='--')

    # Set the x-axis limits to start from 1 and end at the maximum value in your data
    plt.xlim(0.5, max(level_input) + .5)  # Replace max(level_input) with your maximum complexity level

    # Specify the number of ticks you want on the x-axis (e.g., one tick per integer)
    num_ticks = max(level_input) - 1  # Adjust as needed
    plt.xticks(range(1, max(level_input) + 1), range(1, max(level_input) + 1))

    # Set the legend to the right of the graph
    plt.legend(title='Patterns', loc='center left', bbox_to_anchor=(1, 0.5))

    # Label axes and set title
    plt.xlabel('Complexity Level of facade variation')
    plt.ylabel('Complexity Score')
    plt.title('Facade Complexity Analysis per Pattern')

    # Display the grid
    plt.grid(True)
    # plt.grid(axis='x')

    # Specify the relative path to the Graphs directory from the script directory
    relative_graphs_path = os.path.join('..', 'src', 'Graphs')

    # Construct the full file path for saving the PDF
    save_path = os.path.join(script_directory_input, relative_graphs_path, 'complexitygraphrender.pdf')

    # Save the plot as a PDF file
    plt.savefig(save_path, bbox_inches='tight')

    # Show the plot
    plt.show()


# This function plots each pattern separately

def generate_scatter_render_complexity_separate(levels_input, complexity_scores_input, pattern_labels_input,
                                                style_names_input, script_directory_input):
    # Set the desired aspect ratio (16:9)
    aspect_ratio = 12 / 4

    # Calculate the figure width based on the aspect ratio
    fig_width = 12  # You can adjust this value as needed

    # Calculate the corresponding figure height
    fig_height = fig_width / aspect_ratio

    # Create a colormap for styles
    color_ref = ['prism', 'tab20', 'tab20b', 'tab20c', 'Set3']
    # Define the colormap reference directly
    selected_colormap = color_ref[3]
    style_cmap = plt.get_cmap(selected_colormap)  # Change 'tab20' to the desired colormap name

    # Initialize a list to store trendline coefficients for each style
    trend_coefficients_list = []

    # Create a scatter plot for each style
    for style_index, style in enumerate(style_names_input):
        # Filter data points for the current style
        style_mask = [pattern_labels_input[i] == style for i in range(len(pattern_labels_input))]
        style_levels = [levels_input[i] for i in range(len(levels_input)) if style_mask[i]]
        style_complexity_scores = [complexity_scores_input[i] for i in range(len(complexity_scores_input)) if
                                   style_mask[i]]

        # Create a subplot for the current style
        plt.figure(figsize=(fig_width, fig_height))
        plt.scatter(style_levels, style_complexity_scores, color=style_cmap(style_index),
                    label=style)  # Add label to create legend

        # Fit a polynomial trend line for the current style
        trend_coefficients = np.polyfit(style_levels, style_complexity_scores, 2)  # Adjust the degree as needed
        trend_line = np.polyval(trend_coefficients, style_levels)
        trend_coefficients_list.append(trend_coefficients)

        # Plot the trendline for the current style
        plt.plot(style_levels, trend_line, color=style_cmap(style_index), linestyle='--')

        # Customize the subplot
        plt.xlabel('Pattern Complexity Level')
        plt.ylabel('Complexity Score')
        plt.title(f'Facade Complexity Analysis by Level of Complexity ({style})')
        plt.grid(True)

        # Set the x-axis ticks to the range of levels
        plt.xticks(range(1, max(style_levels) + 1))

        # Save the plot as a PDF file
        # save_path = os.path.join(script_directory_input, f'complexitygraphrender_{style}.pdf')
        # plt.savefig(save_path, bbox_inches='tight')
        # plt.show()

        # Specify the relative path to the Graphs directory from the script directory
        relative_graphs_path = os.path.join('..', 'src', 'Graphs')

        # Construct the full file path for saving the PDF
        save_path = os.path.join(script_directory_input, relative_graphs_path, f'complexitygraphrender_{style}.pdf')
        plt.savefig(save_path, bbox_inches='tight')
        plt.show()

    # Now, you can access the trend coefficients for each style from the trend_coefficients_list.
    return trend_coefficients_list
