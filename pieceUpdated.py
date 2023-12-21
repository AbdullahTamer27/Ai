
from pieceGUI import PieceGUI


class Piece() :
    id = 0
    def __init__(self,size):
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

    def createSprite(self,color,x,y):
        return PieceGUI(color,self.size,x,y)


class White(Piece):
    def __init__(self, size):
        super().__init__(size)
        self.team = "White"
    
class Black(Piece):
    def __init__(self,  size):
        super().__init__(size)
        self.team = "Black"
    

    

