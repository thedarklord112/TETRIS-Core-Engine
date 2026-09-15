from typing import List, Tuple

# The 7 classic Tetris shapes defined inside square grids (matrices)
SHAPES = {
    'I': [[0, 0, 0, 0],
,
 ,
          [0, 0, 0, 0]],
          
    'O': [[1, 1],
          [1, 1]],
          
    'T': [[0, 1, 0],
,
          [0, 0, 0]],
          
    'S': [[0, 1, 1],
,
          [0, 0, 0]],
          
    'Z': [[1, 1, 0],
,
          [0, 0, 0]],
          
    'J': [[1, 0, 0],
,
          [0, 0, 0]],
          
    'L': [[0, 0, 1],
,
 ]
}

class Tetromino:
    def __init__(self, shape_type: str):
        if shape_type not in SHAPES:
            raise ValueError(f"Invalid shape type: {shape_type}")
        self.shape_type = shape_type
        # Deep copy of the matrix template
        self.matrix = [row[:] for row in SHAPES[shape_type]]
        # Spawn coordinates (centered horizontally at the top of a 10-column board)
        self.x = 3 if shape_type in ['I', 'O'] else 4
        self.y = 0

    def rotate_clockwise(self) -> List[List[int]]:
        """
        Rotates the matrix 90 degrees clockwise using pure matrix transposition.
        Returns the rotated matrix template without modifying the piece state yet.
        """
        # Transpose matrix (swap rows with columns) and reverse each row
        return [list(row) for row in zip(*self.matrix[::-1])]

    def apply_rotation(self, new_matrix: List[List[int]]):
        """Applies the rotated matrix to the active piece."""
        self.matrix = new_matrix
