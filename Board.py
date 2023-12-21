import pieceUpdated

class Board:
    def __init__(self):
        self.placement_on_board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        piece_sizes = [20, 40, 60, 80]
        # Create White then Black From small to big
        self.whitePieces = []
        self.blackPieces = []
        for i in range(3):
            for size in piece_sizes: 
                white = pieceUpdated.White(size)
                self.whitePieces.append(white)
                black = pieceUpdated.Black(size)
                self.blackPieces.append(black)
        
    def checkList(self):
        print(self.whitePieces)
        
