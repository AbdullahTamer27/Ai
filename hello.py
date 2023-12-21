import pygame
from pieceGUI import Piece

# pygame setup
pygame.init()
width, height = 900, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gobblet Game")
clock = pygame.time.Clock()
running = True

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Board dimensions
rows, cols = 4, 4
cell_size = 600 // cols

# Calculate the starting position for the board to center it
board_start_x = (width - cols * cell_size) // 2
board_start_y = (height - rows * cell_size) // 2

# Sample board data (you would replace this with your actual game state)
board_data = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None]
]

# Draw the game board
def draw_board():
    screen.fill(WHITE)
    
    for row in range(rows):
        for col in range(cols):
            x = board_start_x + col * cell_size
            y = board_start_y + row * cell_size
            pygame.draw.rect(screen, BLACK, (x, y, cell_size, cell_size), 1)
            

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle mouse input for placing or moving pieces
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Calculate the row and column based on mouse position
            col = (mouse_x - board_start_x) // cell_size
            row = (mouse_y - board_start_y) // cell_size
            
            # Check if the clicked cell is within the board bounds
            if 0 <= row < rows and 0 <= col < cols:
                # Perform your logic for placing or moving pieces here
                # You might want to implement a Player class, turn switching, etc.
                # For now, let's just place a piece on the clicked cell
                board_data[row][col] = Piece(BLACK)

    # Update game state and draw the board
    draw_board()

    # RENDER YOUR GAME HERE

    # Flip the display to put your work on the screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
