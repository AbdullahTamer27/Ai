import pieceUpdated

class Board:
    def __init__(self):
        self.placement_on_board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        piece_sizes = [20,40,60,80]
        # Create White then Black From small to big
        self.whitePieces = []
        self.blackPieces = []
        for i in range(3):
            for size in piece_sizes: 
                white = pieceUpdated.White((253, 187, 161), size, 100, 200)
                self.whitePieces.append(white)
                black = pieceUpdated.Black((112, 57, 127), size, 700, 200)
                self.blackPieces.append(black)
                #testing
                white.adf()
                black.adf()
        
    def checkList(self):
        print(self.whitePieces)
        print(self.blackPieces[3].adf())
        




# board = Board()
# board.checkList()
