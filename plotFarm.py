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

    # Define a color map for the visualization
    cmap = plt.cm.get_cmap('Set1', 4)  # 4 distinct colors
    plt.figure(figsize=(10, 6))

    # Draw the farm grid
    plt.imshow(grid, cmap=cmap, interpolation='nearest')
    plt.colorbar(ticks=[0, 1, 2, 3], label='Legend')
    plt.clim(-0.5, 3.5)  # Set color limits

    # Set legend labels
    color_labels = ['Unfarmable', 'Sprinkler', 'Watered', 'Unwatered']
    handles = [plt.Rectangle((0, 0), 1, 1, color=cmap(i / 3)) for i in range(4)]
    plt.legend(handles, color_labels, bbox_to_anchor=(1.05, 1), loc='upper left')

    # Set gridlines
    plt.xticks(np.arange(-0.5, cols, 1), [])
    plt.yticks(np.arange(-0.5, rows, 1), [])
    plt.grid(color='black', linestyle='-', linewidth=1)

    # Display the plot
    plt.title("Farm Sprinkler Placement and Watering")
    plt.show()
    # plt.savefig("farm.png")
