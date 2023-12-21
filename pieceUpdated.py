import pygame

class Piece(pygame.sprite.Sprite) :
    id = 0
    def __init__(self, size, x, y):
        self.idx = Piece.id +1
        Piece.id = Piece.id +1
        super().__init__()
        self.above = [] # list of Pieces above
        self.under = [] # list of Pieces under
        self.pos = (-1,-1) # Position of Piece on Board
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (size // 2, size // 2), size // 2)
        self.rect = self.image.get_rect(center=(x, y))

    def setUnder(under):
        self.under.add(under)

    def setAbove(above):
        self.under.add(above)

    def setPos(pos):
        self.pos = pos

    def adf(self):
        print(self.idx)

class White(Piece):
    def __init__(self, color, size, x, y):
        super().__init__(size, x, y)
        self.team = "White"
    
class Black(Piece):
    def __init__(self, color, size, x, y):
        super().__init__(size, x, y)
        self.team = "Black"
    

    

