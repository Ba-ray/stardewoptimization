import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def plot_result_with_images(farmGrid, sprinkler_placement, watered_tiles, image_paths):
    rows = len(farmGrid)
    cols = len(farmGrid[0])

    # # Create a base grid to visualize farm layout
    # grid = np.zeros((rows, cols))

    # Prepare the figure
    fig , ax = plt.subplots(figsize=(8, 6))

    # Loop through each cell and place images based on classification
    for i in range(rows):
        for j in range(cols):
            if sprinkler_placement[i][j] == 1:
                img = mpimg.imread(image_paths['Iridium Sprinkler'])  # Load sprinkler image
            elif farmGrid[i][j] == 0:
                img = mpimg.imread(image_paths['Unfarmable'])  # Load unfarmable image
            elif watered_tiles[i][j] == 1:
                img = mpimg.imread(image_paths['Watered Crops'])  # Load watered image
                if np.random.choice([True, False]):
                    img = np.fliplr(img)  # Rotate image by 90 degrees
            else:
                img = mpimg.imread(image_paths['Unwatered Crops'])  # Load unwatered image

            # Plot image in the respective grid cell
            ax.imshow(img, extent=[j, j + 1, rows - i - 1, rows - i], aspect='auto')

    # Set gridlines
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.set_xticks(np.arange(0, cols, 1))
    ax.set_yticks(np.arange(0, rows, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True, color='black', linestyle='-', linewidth=0.5)

    # Set limits to match grid size
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)

    # Set aspect ratio to equal for square grid
    ax.set_aspect('equal')

    #  Create custom labels for the used images
    color_labels = ['Iridium Sprinkler', 'Quality Sprinkler', 'Unfarmable', 'Watered Crops', 'Unwatered Crops']

    # Create a list of images to display in the legend
    legend_images = [mpimg.imread(image_paths[label]) for label in color_labels]

    # Create the custom legend with images
    for i, (img, label) in enumerate(zip(legend_images, color_labels)):
        imagebox = OffsetImage(img, zoom=0.25)  # Adjust zoom level to make the images smaller
        ab = AnnotationBbox(imagebox, (1.05, 0.95 - i * 0.06), frameon=False, xycoords=ax.transAxes)
        ax.add_artist(ab)
        ax.text(1.15, 0.95 - i * 0.06, label, va='center', fontsize=12, transform=ax.transAxes)

    # Set title and display
    plt.title("Farm Sprinkler Placement and Watering with Images")
    plt.subplots_adjust(right=0.7)  # Adjust to make space for the legend
    plt.show()
