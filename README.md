# Sudoku Solver

## Description:

This is a Sudoku Solver implemented using Pygame, a Python library for game development. The solver utilizes a backtracking algorithm to find a solution to a given Sudoku puzzle. The user interface allows you to visualize the solving process and interact with the game.

## Requirements:

- Python 3.x
- Pygame library

## Installation:

1. Clone the repository or download the source code.
2. Install the Pygame library by running the following command: `pip install pygame`

## Usage:

1. Run the `main.py` file to start the Sudoku Solver game.
2. The game window will open, displaying the Sudoku board.
3. The board is preloaded with a Sudoku puzzle of medium difficulty.
4. The solving process will be visualized on the screen. The program will attempt to find a solution using a backtracking algorithm.
5. Once a solution is found, the solved puzzle will be displayed on the screen.
6. You can modify the difficulty level of the puzzle by changing the value of the `difficulty` parameter in the `Board` constructor. Available options are "easy" and "medium".
7. To exit the game, click the close button.

## Files:

- `main.py`: The main script that initializes the game and controls the game loop.
- `board.py`: Contains the `Board` class that represents the Sudoku board and implements the solving algorithm.

## License:

This project is licensed under the [MIT License](LICENSE).
