import random
from typing import Optional
from src.board import Board
from src.tetromino import Tetromino

class TetrisGame:
    def __init__(self):
        self.board = Board()
        self.score = 0
        self.lines_cleared = 0
        self.game_over = False
        
        # Available pieces to spawn
        self.piece_types = ['I', 'O', 'T', 'S', 'Z', 'J', 'L']
        self.current_piece: Optional[Tetromino] = None
        
        # Spawn the very first piece
        self.spawn_piece()

    def spawn_piece(self):
        """Generates a random new piece at the top of the board."""
        random_shape = random.choice(self.piece_types)
        self.current_piece = Tetromino(random_shape)

        # If the newly spawned piece instantly collides, it's Game Over!
        if not self.board.is_valid_position(self.current_piece, 0, 0):
            self.game_over = True

    def move_left(self) -> bool:
        """Moves the active piece one column to the left if valid."""
        if self.game_over or not self.current_piece:
            return False
        if self.board.is_valid_position(self.current_piece, -1, 0):
            self.current_piece.x -= 1
            return True
        return False

    def move_right(self) -> bool:
        """Moves the active piece one column to the right if valid."""
        if self.game_over or not self.current_piece:
            return False
        if self.board.is_valid_position(self.current_piece, 1, 0):
            self.current_piece.x += 1
            return True
        return False

    def rotate_piece(self) -> bool:
        """Rotates the active piece clockwise if it doesn't collide with boundaries."""
        if self.game_over or not self.current_piece:
            return False
        
        rotated_matrix = self.current_piece.rotate_clockwise()
        if self.board.is_valid_position(self.current_piece, 0, 0, custom_matrix=rotated_matrix):
            self.current_piece.apply_rotation(rotated_matrix)
            return True
        return False

    def drop_one_line(self) -> bool:
        """
        Forces the piece down by one line (gravity tick).
        Locks the piece and triggers line clears if it hits the bottom.
        """
        if self.game_over or not self.current_piece:
            return False

        # Check if it can safely step down
        if self.board.is_valid_position(self.current_piece, 0, 1):
            self.current_piece.y += 1
            return True
        else:
            # The piece hit something, lock it into the matrix
            self.board.lock_piece(self.current_piece)
            
            # Clear lines and award points using classic scoring mechanics
            cleared = self.board.clear_full_rows()
            if cleared > 0:
                self.lines_cleared += cleared
                self.calculate_score(cleared)
            
            # Bring a new piece into play
            self.spawn_piece()
            return False

    def calculate_score(self, lines: int):
        """Awards points based on traditional Tetris multipliers."""
        scoring_system = {
            1: 100,   # Single
            2: 300,   # Double
            3: 500,   # Triple
            4: 800    # Tetris! (Maximum reward)
        }
        self.score += scoring_system.get(lines, 0)
