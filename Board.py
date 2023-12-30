from pieceGUI import Piece, White,Black
class Board:
    def __init__(self):
        #self.placement_on_board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.placement_on_board = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]

    # def valid_movies(self):
    #     valid_movies = []
    #     for row in self.placement_on_board:
    #         for col in self.placement_on_board[row]:
    #             if self.placement_on_board[row][col] == 0 :
    #                 valid_movies.append(self.placement_on_board[row][col])
    #     print(valid_movies)

#
    def evaluate (self , piece ):
        White_score = 0
        Black_score = 0
        if isinstance(piece,White) :

            countRow = 0
            countCol = 0
            countDiagonalL = 0
            countDiagonalR = 0
            # check legal row
            for row in range (4):
                for i in range(4):
                    try:
                        if type(self.placement_on_board[row][i][-1]) == type(piece):
                            countRow += 1
                    except IndexError as e:
                        # Handle IndexError (list index out of range)
                        pass
                if countRow> White_score :
                     White_score=countRow
                countRow = 0

            # check legal column
            for col in range(4):
                for i in range(4):
                    try:
                        if type(self.placement_on_board[i][col][-1]) == type(piece):
                            countCol += 1
                    except IndexError as e:
                        pass
                if countCol > White_score :
                    White_score =countCol
                countCol=0
                # check legal diagonal left to right

            for i in range(4):
                try:
                    if type(self.placement_on_board[i][i][-1]) == type(piece):
                        countDiagonalL += 1
                except IndexError as e:
                    pass
            if countDiagonalL > White_score:
                White_score = countDiagonalL
            countDiagonalL = 0
                    # check legal diagonal right to left
            for i in range(4):
                try:
                    if type(self.placement_on_board[i][3 - i][-1]) == type(piece):
                        countDiagonalR += 1
                except IndexError as e:
                    pass
            if countDiagonalR > White_score:
                White_score = countDiagonalR
            countDiagonalR = 0

            print ("white -->", White_score)

        elif isinstance(piece,Black) :

            countRow = 0
            countCol = 0
            countDiagonalL = 0
            countDiagonalR = 0
            # check legal row
            for row in range (4):
                for i in range(4):
                    try:
                        if type(self.placement_on_board[row][i][-1]) == type(piece):
                            countRow += 1
                    except IndexError as e:
                        # Handle IndexError (list index out of range)
                        pass
                if countRow> Black_score :
                     Black_score = countRow
                countRow = 0

            # check legal column
            for col in range(4):
                for i in range(4):
                    try:
                        if type(self.placement_on_board[i][col][-1]) == type(piece):
                            countCol += 1
                    except IndexError as e:
                        pass
                if countCol > Black_score :
                    Black_score =countCol
                countCol=0
                # check legal diagonal left to right

            for i in range(4):
                try:
                    if type(self.placement_on_board[i][i][-1]) == type(piece):
                        countDiagonalL += 1
                except IndexError as e:
                    pass
            if countDiagonalL > Black_score:
                Black_score = countDiagonalL
            countDiagonalL = 0
                    # check legal diagonal right to left
            for i in range(4):
                try:
                    if type(self.placement_on_board[i][3 - i][-1]) == type(piece):
                        countDiagonalR += 1
                except IndexError as e:
                    pass
            if countDiagonalR > Black_score:
                Black_score = countDiagonalR
            countDiagonalR = 0

            print("Black -->", Black_score)


    def updatePlacement(self, row, col, piece):
        # piece: going to play
        # Piece is going to eat another piece
        onBoard_piece = self.placement_on_board[row][col]
        if onBoard_piece: 
            # OnBoard Pice is Big
            if onBoard_piece[-1].size >= piece.size:
                print("onboard size: " ,onBoard_piece[-1].size, "piece size: " ,piece.size )
                print("Too small")
                return False
            # OnBoard Piece not big
            # Check illegal move: Eating from outside, and not 3 consequitive
            elif piece.pos == (-1,-1): # piece from outside
                countRow = 0 
                countCol = 0
                countDiagonalL = 0
                countDiagonalR = 0
                # check legal row
                for i in range(4):
                    try:
                        if type(self.placement_on_board[row][i][-1]) == type(onBoard_piece[-1]):
                            countRow += 1
                    except IndexError as e:
                        # Handle IndexError (list index out of range)
                        pass
                # check legal column
                for i in range(4):
                    try:
                        if type(self.placement_on_board[i][col][-1]) == type(onBoard_piece[-1]):
                            countCol += 1
                    except IndexError as e:
                        pass
                # check legal diagonal left to right
                for i in range(4):
                    try:
                        if type(self.placement_on_board[i][i][-1]) == type(onBoard_piece[-1]):
                            countDiagonalL += 1
                    except IndexError as e:
                        pass
                # check legal diagonal right to left
                for i in range(4):
                    try:
                        if type(self.placement_on_board[i][3-i][-1]) == type(onBoard_piece[-1]):
                            countDiagonalR += 1
                    except IndexError as e:
                        pass
                    
                if countRow != 3 and countCol != 3 and countDiagonalR != 3 and countDiagonalL != 3:
                    print("Illegal Move: must be 3 in row or column or diagonal to eat from outside")
                    return False
               
                print(".")
                
        
        # Remove Piece from stackk
        if self.placement_on_board[piece.pos[0]][piece.pos[1]]:
            self.placement_on_board[piece.pos[0]][piece.pos[1]].pop()
        
        # Add Piece to stack
        onBoard_piece.append(piece)
        piece.setPos((row,col))
        
    
    def checkWin(self):
        # Check if win by row
        for row in self.placement_on_board:
            try:
                if all(isinstance(stack[-1],White) for stack in row):
                    print("White Row wins")
                    return True,"White Row wins"
                elif all(isinstance(stack[-1],Black) for stack in row):
                    print("Black Row wins") 
                    return True ,"Black Row wins"
            except IndexError as e:
            # Handle IndexError (list index out of range)
                continue
        # Check if Win by col
        for col in range(4):
            try:
                if all(isinstance(row[col][-1],White) for row in self.placement_on_board): #row[col][top stack]
                    print("White Column wins")
                    return True,"White Column wins"
                elif all(isinstance(row[col][-1],Black)for row in self.placement_on_board):
                    print("Black Column wins") 
                    return True,"Black Column wins"
            except IndexError as e:
            # Handle IndexError (list index out of range)
                continue
        # Check Diagonal win
        try:
            if all(isinstance(self.placement_on_board[i][i][-1], White) for i in range(len(self.placement_on_board))):
                print("White Diagonal wins")
                return True,"White Diagonal wins"
            elif all(isinstance(self.placement_on_board[i][i][-1], Black) for i in range(len(self.placement_on_board))):
                print("Black Diagonal wins") 
                return True,"Black Diagonal wins"
        except IndexError as e:
            # Handle IndexError (list index out of range)
                pass
            
        try:
            if all(isinstance(self.placement_on_board[i][len(self.placement_on_board) - 1 - i][-1],White) for i in range(len(self.placement_on_board))):
                print("White Diagonal wins")
                return True,"White Diagonal wins"
            elif all(isinstance(self.placement_on_board[i][len(self.placement_on_board) - 1 - i][-1], Black) for i in range(len(self.placement_on_board))):
                print("Black Diagonal wins") 
                return True,"Black Diagonal wins"
        except IndexError as e:
            pass
        return False,""
                  
        
    
    def printBoard(self):
        return self.placement_on_board
    
    def reset_board(self):
        self.placement_on_board =  [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]
    
