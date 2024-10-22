import pulp

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

    # print(f"Status: {pulp.LpStatus[status]}")
    print(f"Maximum tiles watered: {pulp.value(problem.objective)}")

    # Draw the farm visualization
    # draw_farm(farmGrid, sprinkler_placement, watered_tiles)
    return sprinkler_placement,watered_tiles
