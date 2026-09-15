from typing import List
from src.tetromino import Tetromino

class Board:
    def __init__(self):
        # A standard Tetris board is 20 rows high by 10 columns wide
        self.rows = 20
        self.cols = 10
        # Initialize an empty board filled with zeros
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def is_valid_position(self, piece: Tetromino, offset_x: int, offset_y: int, custom_matrix: List[List[int]] = None) -> bool:
        """
        Checks if a piece can move or rotate into the designated target position.
        Prevents wall phasing and block overlaps.
        """
        matrix = custom_matrix if custom_matrix is not None else piece.matrix
        target_x = piece.x + offset_x
        target_y = piece.y + offset_y

        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if cell:  # If there is a block in the tetromino template
                    board_x = target_x + c
                    board_y = target_y + r

                    # 1. Boundary checking (Left, Right, Bottom walls)
                    if board_x < 0 or board_x >= self.cols or board_y >= self.rows:
                        return False
                    
                    # Ignore upper spawning area checks out of the screen index
                    if board_y < 0:
                        continue

                    # 2. Block overlap checking
                    if self.grid[board_y][board_x] != 0:
                        return False
        return True

    def lock_piece(self, piece: Tetromino):
        """Fuses the falling piece directly into the board grid state."""
        for r, row in enumerate(piece.matrix):
            for c, cell in enumerate(row):
                if cell:
                    board_x = piece.x + c
                    board_y = piece.y + r
                    if 0 <= board_y < self.rows:
                        self.grid[board_y][board_x] = 1

    def clear_full_rows(self) -> int:
        """
        Scans the board for completely filled horizontal lines.
        Removes them, shifts down upper rows, and returns the number of lines cleared.
        """
        lines_cleared = 0
        new_grid = []

        for row in self.grid:
            # If a row does not contain any 0, it means it is fully packed with blocks
            if 0 not in row:
                lines_cleared += 1
            else:
                new_grid.append(row)

        # Re-inject empty lines at the very top of the grid matrix to replace deleted lines
        for _ in range(lines_cleared):
            new_grid.insert(0, [0 for _ in range(self.cols)])

        self.grid = new_grid
        return lines_cleared
