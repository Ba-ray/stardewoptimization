import matplotlib.pyplot as plt
import numpy as np

def plot_result(farmGrid, sprinkler_placement, watered_tiles):
    rows = len(farmGrid)
    cols = len(farmGrid[0])

    # Create a visualization grid using numpy
    grid = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            if sprinkler_placement[i][j] == 1:  # Sprinkler placed
                grid[i][j] = 1
            elif farmGrid[i][j] == 0:        # Unfarmable land
                grid[i][j] = 0
            elif watered_tiles[i][j] == 1:  # Watered farmable land
                grid[i][j] = 2
            else:                           # Unwatered farmable land
                grid[i][j] = 3

    # Define a custom color map for the visualization with more pleasing colors
    cmap = plt.cm.colors.ListedColormap(['black', 'orange', 'deepskyblue', 'saddlebrown'])  # Custom colors

    plt.figure(figsize=(12, 8))

    # Draw the farm grid
    plt.imshow(grid, cmap=cmap, interpolation='none')
    
    # Adjust colorbar position and size to avoid overlap
    cbar = plt.colorbar(ticks=[0, 1, 2, 3], label='Legend', shrink=0.8)
    plt.clim(-0.5, 3.5)  # Set color limits

    # Set legend labels with better color descriptions and place outside the plot
    color_labels = ['Unfarmable (Black)', 'Sprinkler (Orange)', 'Watered (Sky Blue)', 'Unwatered (Brown)']
    handles = [plt.Rectangle((0, 0), 1, 1, color=cmap(i)) for i in range(4)]
    
    # Position legend to the right and outside the plot
    plt.legend(handles, color_labels, bbox_to_anchor=(1.05, 0.5), loc='center left', borderaxespad=0, fontsize=10)

    # Set gridlines with enhanced visibility
    plt.xticks(np.arange(-0.5, cols, 1), [])
    plt.yticks(np.arange(-0.5, rows, 1), [])
    plt.grid(color='white', linestyle='-', linewidth=1.5)

    # Display the plot with a more descriptive title
    plt.title("Optimized Farm Sprinkler Placement and Watering", fontsize=16, pad=20)
    
    # Tight layout for better spacing
    plt.tight_layout()
    
    plt.show()
    # plt.savefig("farm.png")
