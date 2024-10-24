import ILP
import plotFarm
import drawGrid

farm = drawGrid.get_farm_grid(20,20)

sprinkler_placement,watered_tiles = ILP.solve(farm)

# Define image paths for each category
image_paths = {
    'Unfarmable': './Images/Unfarmable.png',
    'Iridium Sprinkler': './Images/Iridium Sprinkler.png',
    'Watered Crops': './Images/Watered Crops.png',
    'Unwatered Crops': './Images/Unwatered Crops.png',
    'Quality Sprinkler': './Images/Quality Sprinkler.png'
}

# Call the function to plot
plotFarm.plot_result_with_images(farm, sprinkler_placement, watered_tiles, image_paths)