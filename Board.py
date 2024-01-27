from pieceGUI import Piece, White,Black
import copy
class Board:
    def __init__(self):
        #self.placement_on_board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.placement_on_board = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.whitePieces = []
        self.blackPieces = []
        self.firstW = []
        self.firstB = []
        self.secondW = []
        self.secondB = []
        self.thirdW = []
        self.thirdB = []



    def evaluate (self , player ):
        White_score = 0
        Black_score = 0
        if player:
            piece = White((253, 187, 161), 3, 3, 3)
        else:
            piece = Black((112, 57, 127), 3, 3, 3)
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

          #  print ("white -->", White_score)
            return White_score

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

           # print("Black -->", Black_score)
            return Black_score


    def simulatePlacement(self, row, col, piece):
        # piece: going to play
        # Piece is going to eat another piece
        onBoard_piece = self.placement_on_board[row][col]
        if onBoard_piece: 
            # OnBoard Pice is Big
            if onBoard_piece[-1].size >= piece.size:
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
                    return False
        
        if self.placement_on_board[piece.pos[0]][piece.pos[1]]:
            self.placement_on_board[piece.pos[0]][piece.pos[1]].pop()
            if self.placement_on_board[piece.pos[0]][piece.pos[1]]:
                try:
                    self.placement_on_board[piece.pos[0]][piece.pos[1]][-1].isMovable = True
                except IndexError as e:
                    print("error in setting ", piece.idx)
                    pass
        return True

        
    
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

    def onTop(self, piece, row, col):
        if(row,col) == (-1,-1) or (row,col) == (3,3) :
            return True
        onBoard_piece = self.placement_on_board[row][col]
        return onBoard_piece and onBoard_piece[-1] is piece


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
            
            
        if piece.pos == (-1,-1):
            #print("entered -1, -1 if")
            try:
                if piece in self.firstW:
                    self.firstW.pop()
                    #print(self.firstW)
                    self.firstW[-1].isMovable = True
                elif piece in self.secondW:
                    self.secondW.pop()
                    #print(self.secondW)
                    self.secondW[-1].isMovable = True
                elif piece in self.thirdW:
                    self.thirdW.pop()
                   # print(self.thirdW)
                    self.thirdW[-1].isMovable = True
                elif piece in self.firstB:
                    self.firstB.pop()
                   # print(self.firstB)
                    self.firstB[-1].isMovable = True
                elif piece in self.secondB:
                    self.secondB.pop()
                    #print(self.secondB)
                    self.secondB[-1].isMovable = True
                elif piece in self.thirdB:
                    self.thirdB.pop()
                    #print(self.thirdB)
                    self.thirdB[-1].isMovable = True
            except IndexError as e:
                print("error", piece.idx)
                pass
        
        # Remove Piece from stackk
        if self.placement_on_board[piece.pos[0]][piece.pos[1]]:
            self.placement_on_board[piece.pos[0]][piece.pos[1]].pop()
            if self.placement_on_board[piece.pos[0]][piece.pos[1]]:
                try:
                    self.placement_on_board[piece.pos[0]][piece.pos[1]][-1].isMovable = True
                except IndexError as e:
                    print("error in setting ", piece.idx)
                    pass
        
        # Add Piece to stack
        try:
            onBoard_piece.append(piece)
            if onBoard_piece[-2]:
                onBoard_piece[-2].isMovable = False
        except IndexError:
            pass
            
        piece.setPos((row,col))