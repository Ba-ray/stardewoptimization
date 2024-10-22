import pygame

# Constants
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Helper function to draw the grid
def draw_grid(grid, screen, rows, cols, pixel_size, submit_button, toggle_button):
    screen.fill(BLACK)
    for y in range(rows):
        for x in range(cols):
            color = WHITE if grid[y][x] == 1 else BLACK
            pygame.draw.rect(screen, color, (x * pixel_size, y * pixel_size, pixel_size, pixel_size))
            pygame.draw.rect(screen, WHITE, (x * pixel_size, y * pixel_size, pixel_size, pixel_size), 1)  # Draw border
    pygame.draw.rect(screen, WHITE, submit_button)
    pygame.draw.rect(screen, WHITE, toggle_button)
    pygame.display.flip()

def get_farm_grid(rows, cols):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
    pygame.display.set_caption("StardewOptimization")

    # Calculate pixel dimensions based on matrix size
    PIXEL_SIZE = min(WIDTH // cols, HEIGHT // rows)

    # Create a grid with binary values (0 for black, 1 for white)
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Drag feature
    current_value = 1  # 1 = White (default), 0 = Black

    # Submit and toggle buttons
    submit_button = pygame.Rect(WIDTH - 100, HEIGHT - 50, 80, 30)
    toggle_button = pygame.Rect(WIDTH - 100, HEIGHT - 100, 80, 30)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                # Handle button clicks
                if submit_button.collidepoint(event.pos):
                    pygame.quit()
                    return grid
                elif toggle_button.collidepoint(event.pos):
                    # Toggle between setting cells to 0 or 1
                    current_value = 1 - current_value  # Switch between 0 and 1
                else:
                    # Modify the clicked cell
                    grid_x = x // PIXEL_SIZE
                    grid_y = y // PIXEL_SIZE
                    if 0 <= grid_x < cols and 0 <= grid_y < rows:
                        grid[grid_y][grid_x] = current_value  # Set cell to current value

            elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                grid_x = x // PIXEL_SIZE
                grid_y = y // PIXEL_SIZE
                if 0 <= grid_x < cols and 0 <= grid_y < rows:
                    grid[grid_y][grid_x] = current_value  # Set cell to current value

        draw_grid(grid, screen, rows, cols, PIXEL_SIZE, submit_button, toggle_button)

# Quit Pygame
# pygame.quit()
