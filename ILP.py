import pulp
import matplotlib.pyplot as plt
import numpy as np

def solve(farmGrid):
    # Grid dimensions
    rows = len(farmGrid)
    cols = len(farmGrid[0])

    # Initialize the optimization problem
    problem = pulp.LpProblem("Sprinkler_Optimization", pulp.LpMaximize)

    # Variables for sprinklers and watered cells
    sprinklers = [
        [pulp.LpVariable(f"Sprinkler_cell({row},{col})", cat="Binary")
         for col in range(cols)] for row in range(rows)
    ]

    watered = [
        [pulp.LpVariable(f"Watered_cell({i},{j})", cat="Binary")
         for j in range(cols)] for i in range(rows)
    ]

    # Objective Function: Maximize the number of watered farmable cells
    problem += pulp.lpSum(
        watered[row][col] for row in range(rows) for col in range(cols)
        if farmGrid[row][col] == 1  # Only farmable land contributes
    ) - pulp.lpSum(
        sprinklers[row][col] for row in range(rows) for col in range(cols)
    )

    # Constraint: A farmable cell can only be watered if at least one sprinkler is in its 5x5 range
    for i in range(rows):
        for j in range(cols):
            if farmGrid[i][j] == 1:  # Apply only to farmable cells
                problem += (
                    watered[i][j] <= pulp.lpSum(
                        sprinklers[di][dj]
                        for di in range(max(0, i - 2), min(rows, i + 3))
                        for dj in range(max(0, j - 2), min(cols, j + 3))
                        if (di, dj) != (i, j)  # Exclude the sprinkler in the same cell
                    )
                )

    # Constraint: A cell with a sprinkler cannot be marked as watered
    for i in range(rows):
        for j in range(cols):
            problem += watered[i][j] <= 1 - sprinklers[i][j]

    # Solve the problem
    status = problem.solve()

    # Prepare the results
    sprinkler_placement = [[int(pulp.value(sprinklers[i][j])) for j in range(cols)] for i in range(rows)]
    watered_tiles = [[int(pulp.value(watered[i][j])) for j in range(cols)] for i in range(rows)]

    print(f"Status: {pulp.LpStatus[status]}")
    print(f"Maximum tiles watered: {pulp.value(problem.objective)}")

    # Draw the farm visualization
    draw_farm(farmGrid, sprinkler_placement, watered_tiles)

def draw_farm(farmGrid, sprinkler_placement, watered_tiles):
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
    # plt.show()
    plt.savefig("farm.png")


# Input farm grid
grid = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

# Solve the problem and visualize the result
solve(grid)
