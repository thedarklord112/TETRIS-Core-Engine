import os
import sys
from src.game import TetrisGame

def draw_screen(game: TetrisGame):
    """Clears the console and renders the full Tetris board array via text."""
    # Clear terminal based on OS
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("🔳 TETRIS CORE ENGINE RUNNING 🔳")
    print(f"🏆 SCORE: {game.score} | 🎯 LINES: {game.lines_cleared}")
    print("=" * 24)

    # Clone the board grid to overlay the active falling piece
    display_grid = [row[:] for row in game.board.grid]
    
    if game.current_piece and not game.game_over:
        p = game.current_piece
        for r, row in enumerate(p.matrix):
            for c, cell in enumerate(row):
                if cell:
                    board_y = p.y + r
                    board_x = p.x + c
                    if 0 <= board_y < game.board.rows and 0 <= board_x < game.board.cols:
                        display_grid[board_y][board_x] = 2  # 2 represents active piece

    # Render matrix to text symbols
    for row in display_grid:
        line_str = "│"
        for cell in row:
            if cell == 1:
                line_str += "◼ "  # Locked block
            elif cell == 2:
                line_str += "▣ "  # Active piece block
            else:
                line_str += ". "  # Empty spaces
        line_str += "│"
        print(line_str)
        
    print("=" * 24)
    print("Controls: [a] Left  [d] Right  [w] Rotate  [s] Drop  [q] Quit")

def main():
    game = TetrisGame()
    
    while not game.game_over:
        draw_screen(game)
        
        # Get immediate keyboard input
        user_move = input("\nEnter Action: ").strip().lower()
        
        if user_move == 'a':
            game.move_left()
        elif user_move == 'd':
            game.move_right()
        elif user_move == 'w':
            game.rotate_piece()
        elif user_move == 's':
            game.drop_one_line()
        elif user_move == 'q':
            print("\nGame session closed. Thanks for playing!")
            sys.exit()
            
        # Simulate natural gravity step after user command
        game.drop_one_line()

    # If loop breaks, it's Game Over
    draw_screen(game)
    print("\n💀 GAME OVER! The stack reached the top. 💀")

if __name__ == "__main__":
    main()
