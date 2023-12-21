import pygame
import Board
import pieceUpdated
from sys import exit


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


piece_sizes = [20,40,60,80]

coordinates_on_board = [
    [(260,200),(355,200),(445,200),(540,200)],
    [(260,300),(355,300),(445,300),(540,300)],
    [(260,400),(355,400),(445,400),(540,400)],
    [(260,500),(355,500),(445,500),(540,500)]
]

brd = Board.Board()

x_initial_r = 700
x_initial_l = 100
y_initial = 200
all_pieces = pygame.sprite.Group()
for piece in brd.whitePieces:
    all_pieces.add(piece)
for piece in brd.blackPieces:
    all_pieces.add(piece)

# for i in range(3):
#     for size in piece_sizes:
#         left = Piece((253, 187, 161), size, x_initial_l, y_initial)
#         right = Piece((112, 57, 127), size, x_initial_r, y_initial)
#         all_pieces.add(right)
#         all_pieces.add(left)
#     y_initial += 130

selected_piece = None
dragging = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                for piece in all_pieces:
                    if piece.rect.collidepoint(event.pos):
                        selected_piece = piece
                        dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                min_distance = float('inf')
                closest_position = None
                for row, positions in enumerate(coordinates_on_board):
                    for col, pos in enumerate(positions):
                        distance = pygame.math.Vector2(pos).distance_to(pygame.math.Vector2(pygame.mouse.get_pos()))
                        if distance < min_distance:
                            min_distance = distance
                            closest_position = (row, col)
                if closest_position is not None:
                    row, col = closest_position
                    if selected_piece is not None:
                        selected_piece.rect.center = coordinates_on_board[row][col]
                        print(row,col)

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

    pygame.display.update()
    clock.tick(60)
