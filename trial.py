import pygame
from sys import exit
from pieceGUI import Piece, White, Black
from Board import Board
# Game state variables
# Constants for game states
MENU = 0
GAME = 1

game_state = MENU
game_mode = None
difficulty = None

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Gobblet Game")
clock = pygame.time.Clock()

background = pygame.image.load('graphics/board.jpg').convert_alpha()
background_rec = background.get_rect(center=(400, 350))
color1 = (249,122,136)  # cream
color2 = (204,132,216)  # purple
color3 = (100,72,96)  # purple

test_font = pygame.font.Font(None, 70)
text_surface = test_font.render('Gobblet', False, (23, 2, 24))
text_rec = text_surface.get_rect(center=(400, 100))


new_game_button_rect = pygame.Rect(300, 400, 200, 50)
exit_button_rect = pygame.Rect(300, 470, 200, 50)


piece_sizes = [20,40,60,80]


coordinates_on_board = [
    [(260,200),(355,200),(445,200),(540,200)],
    [(260,300),(355,300),(445,300),(540,300)],
    [(260,400),(355,400),(445,400),(540,400)],
    [(260,500),(355,500),(445,500),(540,500)]
]



white_pieces = pygame.sprite.Group()
black_pieces = pygame.sprite.Group()
all_pieces = pygame.sprite.Group()
board = Board()
def reset_positions():
    x_initial_r = 700
    x_initial_l = 100
    y_initial = 200
    for size in piece_sizes:
        for i in range(3):
            left = White((253, 187, 161), size, x_initial_l, y_initial)
            right = Black((112, 57, 127), size, x_initial_r, y_initial)
            white_pieces.add(left)
            black_pieces.add(right)
            all_pieces.add(left)
            all_pieces.add(right)
            y_initial += 130
        y_initial = 200
reset_positions()
selected_piece = None
old_position = None
dragging = False
Playerturn = True
game_over = False
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and  Playerturn:  # Left mouse button and its player 1s turn
                for piece in white_pieces:
                    if piece.rect.collidepoint(event.pos):
                        selected_piece = piece
                        dragging = True
            elif event.button == 1 and not Playerturn:
                for piece in black_pieces:
                    if piece.rect.collidepoint(event.pos):
                        selected_piece = piece
                        dragging = True

        elif game_state == MENU:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_mode = "Player vs Player"
                    game_state = GAME
                elif event.key == pygame.K_2:
                    game_mode = "Player vs AI(easy)"
                    game_state = GAME
                elif event.key == pygame.K_3:
                    game_mode = "Player vs AI(hard)"
                    game_state = GAME    
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
    
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                min_distance = float('inf')
                closest_position = None
                for row, positions in enumerate(coordinates_on_board):
                    for col, pos in enumerate(positions):
                        distance = pygame.math.Vector2(pos).distance_to(pygame.math.Vector2(pygame.mouse.get_pos()))
                        if distance < min_distance :
                            min_distance = distance
                            closest_position = (row, col)
                            
                if closest_position is not None:
                    row, col = closest_position
                    if selected_piece is not None:
                        if board.updatePlacement(row, col, selected_piece) == False:
                            selected_piece.rect.center = selected_piece.oldPosition
                            continue
                        selected_piece.rect.center = coordinates_on_board[row][col]
                        selected_piece.setOldPosition(coordinates_on_board[row][col])
                        game_over,winner = board.checkWin()
                        
                        Playerturn = not Playerturn
               
                     
                selected_piece = None

    if dragging and selected_piece:
        selected_piece.rect.center = pygame.mouse.get_pos()

    screen.fill((255, 255, 255))
    for y in range(600):
        current_color = (
            int((color2[0] - color1[0]) * y / 600) + color1[0],
            int((color2[1] - color1[1]) * y / 600) + color1[1],
            int((color2[2] - color1[2]) * y / 600) + color1[2]
        )
        pygame.draw.line(screen, current_color, (0, y), (800, y))

    screen.blit(background, background_rec)
    all_pieces.draw(screen)
    screen.blit(text_surface, text_rec)

    if game_state == MENU:
        # Draw menu text
        screen.fill((255, 255, 255))
        menu_font = pygame.font.Font(None, 36)
        menu_text1 = menu_font.render("press 1 - Player vs Player", True, (0, 0, 0))
        menu_text2 = menu_font.render("press 2 - Player vs AI(easy)", True, (0, 0, 0))
        menu_text3 = menu_font.render("press 3 - Player vs AI(Hard)", True, (0, 0, 0))
        menu_text4 = menu_font.render("Press ESC to exit", True, (0, 0, 0))
        screen.blit(menu_text1, (300, 300))
        screen.blit(menu_text2, (300, 340))
        screen.blit(menu_text3, (300, 380))
        screen.blit(menu_text4, (300, 420))



#game over screen
    if game_over:
        # Display the winning message and handle the end of the game
        screen.fill((0, 0, 0))
        winner_font = pygame.font.Font(None, 50)
        winner_text = winner_font.render(winner, True, (255, 0, 0))
        screen.blit(winner_text, (300, 300))

        # Draw new game and exit buttons
        pygame.draw.rect(screen, (0, 255, 0), new_game_button_rect)  # Green button for new game
        pygame.draw.rect(screen, (255, 0, 0), exit_button_rect)  # Red button for exit

        # Text on buttons
        button_font = pygame.font.Font(None, 36)
        new_game_text = button_font.render("New Game", True, (0, 0, 0))
        exit_text = button_font.render("Exit", True, (0, 0, 0))

        screen.blit(new_game_text, (new_game_button_rect.x + 20, new_game_button_rect.y + 15))
        screen.blit(exit_text, (exit_button_rect.x + 80, exit_button_rect.y + 15))

        # Check for button clicks
        mouse_pos = pygame.mouse.get_pos()
        if new_game_button_rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Start a new game when the new game button is clicked
                game_over = False
                all_pieces.empty()
                reset_positions()
                board.reset_board()
                
        elif exit_button_rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pygame.quit()
                exit()

    pygame.display.update()
    clock.tick(60)
