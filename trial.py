import pygame
from sys import exit
from MINMAX.AI import AI
from pieceGUI import White, Black
from Board import Board
from MINMAX.algorithm import minimax, testsimulation, compare
# Game state variables
# Constants for game states

# def can_place_piece(board, row, col, piece):
#     onBoard_piece = board.placement_on_board[row][col]
#     if onBoard_piece[-1].size >= piece.size:
#         print("onboard size: ", onBoard_piece[-1].size, "piece size: ", piece.size)
#         print("Too small")
#         return False
#     return True
#
# def all_moves(board, piece):
#     moves = []
#     for row in range(len(board)):
#         for col in range(len(board[row])):
#             if can_place_piece(board, row, col, piece):
#                 # Assuming you have a function to clone the board state
#                 new_board = clone_board(board)
#                 place_piece(new_board, row, col, piece)
#                 moves.append(new_board)
#             if can_gobble(board, row, col, piece):
#                 # Consider all gobble moves
#                 for new_board in generate_gobble_moves(board, row, col, piece):
#                     moves.append(new_board)
#     return moves
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
Ai = AI(board)
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
            board.whitePieces.append(left)
            board.blackPieces.append(right)
            all_pieces.add(left)
            all_pieces.add(right)
            y_initial += 130
        y_initial = 200
    # 1234
    # 1 1 1             1 1 1 2 2 2 3 3 3 4 4 4
    # 2 2 2             first stack indexs: 0 3 6 9
    # 3 3 3             second stack    :   1 4 7 10
    # 4 4 4             third stack :       2 5 8 11

#white_pieces.sprites()[9].under = [white_pieces.sprites()[0], white_pieces.sprites()[3], white_pieces.sprites()[6]]

reset_positions()

board.firstW = [white_pieces.sprites()[0], white_pieces.sprites()[3], white_pieces.sprites()[6], white_pieces.sprites()[9]]
board.secondW = [white_pieces.sprites()[1], white_pieces.sprites()[4], white_pieces.sprites()[7], white_pieces.sprites()[10]]
board.thirdW = [white_pieces.sprites()[2], white_pieces.sprites()[5], white_pieces.sprites()[8], white_pieces.sprites()[11]]

board.firstB =[black_pieces.sprites()[0], black_pieces.sprites()[3], black_pieces.sprites()[6], black_pieces.sprites()[9]] 
board.secondB =[black_pieces.sprites()[1], black_pieces.sprites()[4], black_pieces.sprites()[7], black_pieces.sprites()[10]] 
board.thirdB =[black_pieces.sprites()[2], black_pieces.sprites()[5], black_pieces.sprites()[8], black_pieces.sprites()[11]]

print(board.firstW)
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
                    if piece.rect.collidepoint(event.pos)and board.onTop(piece, piece.pos[0], piece.pos[1]):
                        selected_piece = piece
                        dragging = True
            elif event.button == 1 and not Playerturn:
                for piece in black_pieces:
                    if piece.rect.collidepoint(event.pos) and board.onTop(piece, piece.pos[0], piece.pos[1]):
                        selected_piece = piece
                        dragging = True

        elif game_state == MENU:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_mode = "PvP"
                    game_state = GAME
                elif event.key == pygame.K_2:
                    game_mode = "easy"
                    game_state = GAME
                elif event.key == pygame.K_3:
                    game_mode = "hard"
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
                        board.evaluate(selected_piece)
                        selected_piece.rect.center = coordinates_on_board[row][col]
                        selected_piece.setOldPosition(coordinates_on_board[row][col])
                        game_over,winner = board.checkWin()
                        
                        #testsimulation(board)
                        
                        x = minimax(board,1,Playerturn)
                        #print(x[1].printBoard())
                        print("______________________________")
                        print("evaluation: ",x[0], "Best move: ",x[1].printBoard())
                        Playerturn = not Playerturn
                        if not Playerturn:
                            moved_piece, newpos = compare(board,x[1])
                            if board.updatePlacement(newpos[0], newpos[1], moved_piece) == False:
                                moved_piece.rect.center = moved_piece.oldPosition
                                continue
                            moved_piece.rect.center = coordinates_on_board[newpos[0]][newpos[1]]
                            moved_piece.setOldPosition(coordinates_on_board[newpos[0]][newpos[1]])
                            Playerturn = not Playerturn
                        
                        Ai.board = board
                        #Ai.get_all_moves(Playerturn)
                        # CALL MINIMAX  
                        #Ai.board = board
                        # for piece in all_pieces:
                        #     print(piece.idx, piece.isMovable)
                        # print(".")
                        if(game_mode == 'PvP'):
                            continue
                        elif(game_mode == 'easy'):
                            #Playerturn = not Playerturn
                            continue
                        elif(game_mode == 'hard'):
                            
                            continue

                
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
                game_state = MENU
                Playerturn = True
                
        elif exit_button_rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pygame.quit()
                exit()

    # board.valid_movies()
    pygame.display.update()

    clock.tick(60)

