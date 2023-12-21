import pygame

class Piece(pygame.sprite.Sprite) :
    id = 0
    def __init__(self, color,size,x,y):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (size // 2, size // 2), size // 2)
        self.rect = self.image.get_rect(center=(x, y))
        self.idx = Piece.id +1
        Piece.id = Piece.id +1
        self.above = [] # list of Pieces above
        self.under = [] # list of Pieces under
        self.pos = (-1,-1) # Position of Piece on Board
        self.size = size


    def setUnder(self,under):
        self.under.add(under)

    def setAbove(self,above):
        self.above.add(above)

    def setPos(self,pos):
        self.pos = pos

    def adf(self):
        print(self.idx)


class White(Piece):
    def __init__(self, size):
        super().__init__(size)
        self.team = "White"
    
class Black(Piece):
    def __init__(self,  size):
        super().__init__(size)
        self.team = "Black"
    

