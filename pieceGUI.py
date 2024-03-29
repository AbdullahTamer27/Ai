import pygame

class Piece(pygame.sprite.Sprite) :
    id = 0
    def __init__(self, color,size,x,y):
        super().__init__()
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (size // 2, size // 2), size // 2)
        self.rect = self.image.get_rect(center=(x, y))
        self.x = x
        self.y = y
        self.oldPosition = (x,y)
        self.idx = (Piece.id +1) % 25
        Piece.id = Piece.id +1
        # if Piece.id == 24:
        #     Piece.id = 0
        self.above = [] # list of Pieces above
        self.under = [] # list of Pieces under
        self.pos = (None,None) # Position of Piece on Board
        self.size = size
        self.isMovable = False
        
        if self.size == 80:
            self.isMovable = True
        
    def appendUnder(self,under):
        self.under.append(under)

    def appendAbove(self,above):
        self.above.append(above)

    def setPos(self,pos):
        self.pos = pos

    def getID(self):
        return self.idx
    
    def setOldPosition(self, position):
        self.oldPosition = position
        
    def __str__(self):
        return self.idx


class White(Piece):
    def __init__(self, color,size,x,y):
        super().__init__(color,size,x,y)
        self.team = "White"
    
class Black(Piece):
    def __init__(self,  color,size,x,y):
        super().__init__(color,size,x,y)
        self.team = "Black"
    

