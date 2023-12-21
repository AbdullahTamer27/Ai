from pieceGUI import Piece
class Board:
    def __init__(self):
        #self.placement_on_board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.placement_on_board = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        
    def updatePlacement(self, row, col, piece):
        # piece: going to play
        onBoard_piece = self.placement_on_board[row][col]
        if onBoard_piece: #there is already onBoard_piece
            if onBoard_piece[-1].size >= piece.size:
                print("onboard size: " ,onBoard_piece[-1].size, "piece size: " ,piece.size )
                print("Too small")
                return False
        
        onBoard_piece.append(piece)
        piece.setPos((row,col))
        
            # piece.appendUnder(onBoard_piece)
            # onBoard_piece.appendAbove(piece)
        # self.placement_on_board[row][col] = piece
        # piece.setPos((row,col))
        
    
    def printBoard(self):
        return self.placement_on_board
    
    
