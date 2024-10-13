#include <iostream>
#include <vector>
#include <algorithm>
#include <SFML/Graphics.hpp>


const int N=5;
const int M=5;

const int SPRINKLER_RADIUS = 2; //Sprinkler can water 24 crops around it (5x5 grid)

//Farm size = N x M
// 10 x 12 farmable land with 2 unfarmable padding space


const int CELL_SIZE = 40;

//Types of cells:
// W : Watered
// F : Farmable
// S : Sprinkler
// D : DeadSpace


// Check if a sprinkler can be placed at (x, y) without overlap
bool canPlaceSprinkler(int x, int y, std::vector<std::vector<char>>& grid) {
    for (int i = x - SPRINKLER_RADIUS; i <= x + SPRINKLER_RADIUS; ++i) {
        for (int j = y - SPRINKLER_RADIUS; j <= y + SPRINKLER_RADIUS; ++j) {
            if (i >= 0 && i < N && j >= 0 && j < M && (grid[i][j] == 'S' || grid[i][j] == 'W'))
                return false; // Overlap detected
        }
    }
    return true;
}

void placeSprinkler(int x, int y, std::vector<std::vector<char>>& grid) {
    grid[x][y] = 'S';
    for (int i = x - SPRINKLER_RADIUS; i <= x + SPRINKLER_RADIUS; ++i) {
        for (int j = y - SPRINKLER_RADIUS; j <= y + SPRINKLER_RADIUS; ++j) {
            if (i >= 0 && i < N && j >= 0 && j < M && grid[i][j] == 'F')
                grid[i][j] = 'W';
        }
    }
}

void optimizeSprinklers(std::vector<std::vector<char>>& grid) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            // Place sprinklers only on dead spaces or farmable land
            if ((grid[i][j] == 'D' || grid[i][j] == 'F') && canPlaceSprinkler(i, j, grid)) {
                placeSprinkler(i, j, grid);
            }
        }
    }
}



void drawGrid(const std::vector<std::vector<char>>& grid, sf::RenderWindow& window) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            sf::RectangleShape cell(sf::Vector2f(CELL_SIZE, CELL_SIZE));
            cell.setPosition(j * CELL_SIZE, i * CELL_SIZE);

            // Set the color based on the cell type
            if (grid[i][j] == 'W')
                cell.setFillColor(sf::Color::Blue);  // Watered crop
            else if (grid[i][j] == 'F')
                cell.setFillColor(sf::Color::Green);  // Farmable land
            else if (grid[i][j] == 'S')
                cell.setFillColor(sf::Color::Yellow);  // Sprinkler
            else
                cell.setFillColor(sf::Color(105, 105, 105));  // Dead space (Gray)

            cell.setOutlineThickness(1);
            cell.setOutlineColor(sf::Color::Black);
            window.draw(cell);
        }
    }
}

int main(){
    // 14 x 16
    // std::vector<std::vector<char>> farm = {
    //     {'D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D'},
    //     {'D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D'},
    //     {'D','D','F','F','F','F','F','F','F','F','F','F','F','F','D','D'},
    //     {'D','D','F','F','F','F','F','F','F','F','F','F','F','F','D','D'},
    //     {'D','D','F','F','F','F','F','F','F','F','F','F','F','F','D','D'},
    //     {'D','D','F','F','F','F','F','F','F','F','F','F','F','F','D','D'},
    //     {'D','D','F','F','F','F','F','F','F','F','F','F','F','F','D','D'},
    //     {'D','D','F','F','F','F','F','F','F','F','F','F','F','F','D','D'},
    //     {'D','D','F','F','F','F','F','F','F','F','F','F','F','F','D','D'},
    //     {'D','D','F','F','F','F','F','F','F','F','F','F','F','F','D','D'},
    //     {'D','D','F','F','F','F','F','F','F','F','F','F','F','F','D','D'},
    //     {'D','D','F','F','F','F','F','F','F','F','F','F','F','F','D','D'},
    //     {'D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D'},
    //     {'D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D'}
    // };

    std::vector<std::vector<char>> farm = {
        {'F','F','F','F','F'},
        {'F','F','F','F','F'},
        {'F','F','F','F','F'},
        {'F','F','F','F','F'},
        {'F','F','F','F','F'}
    };

    optimizeSprinklers(farm);

    sf::RenderWindow window(sf::VideoMode(M * CELL_SIZE, N * CELL_SIZE), "Farm Grid");
    
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear();
        drawGrid(farm, window);
        window.display();
    }
}



// maximize watered space

// => minimal number of sprinklers used (cost)