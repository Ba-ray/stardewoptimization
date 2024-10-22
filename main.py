import ILP
import plotFarm
import drawGrid

farm = drawGrid.get_farm_grid(20,20)

sprinkler_placement,watered_tiles = ILP.solve(farm)

plotFarm.plot_result(farm, sprinkler_placement, watered_tiles)