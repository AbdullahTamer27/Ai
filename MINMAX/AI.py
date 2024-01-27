from pieceGUI import Piece, White,Black
from Board import Board
class AI:
    def __init__(self, board):
        # self.placement_on_board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.board = board
        
    def all_moves(self, piece):
        #print(piece.idx, piece.size)
        
        # playerturn = true then white turn
        # playerturn = false then black turn
        moves = []
        for row in range(4):
            for col in range(4):
                if self.can_move(piece, row, col):  # Ensure the move is legal
                    new_board = self.clone_board()  # Create a new board state
                    test = new_board.simulatePlacement(row, col, piece)
                    if test:
                        new_board.placement_on_board[row][col].append(piece)
                    moves.append(new_board)  # Add the new board state to moves list
        # for move in moves:
        #     for row in move.placement_on_board:
        #         print(row)
        #     print('.')
        # print('\n\n---------------------------------------------\n\n')
        return moves
    
    def get_all_moves(self, playerturn):
        new_board = self.clone_board()
        output = []
        if playerturn: 
            for whitePiece in new_board.whitePieces:
                if whitePiece.isMovable:
                     output.append(self.all_moves(whitePiece))

        elif not playerturn:
            for blackPiece in new_board.blackPieces:
                if blackPiece.isMovable:
                     output.append(self.all_moves(blackPiece))
        return output

    def get_player_pieces(self, pieces):
        # Return a list of all pieces belonging to 'player' that can be moved.
        # This might involve checking your piece storage structure and ensuring the pieces are active/not already played.
        if isinstance(pieces,White):
            return self.board.whitePieces
        if isinstance(pieces,Black):
            return self.board.blackPieces

    def can_move(self, piece, row, col):
        # Determine if 'piece' can legally move to (row, col) on the current board.
        # Include logic for checking if the piece can gobble, move into an empty space, etc.
        onBoard_piece = self.board.placement_on_board[row][col]
        
        if onBoard_piece:
            if onBoard_piece[-1] == piece:
                return True
            # OnBoard Piece is Big
            if onBoard_piece[-1].size >= piece.size and id(piece) != id(onBoard_piece[-1]):
                return False
            # OnBoard Piece not big
            # Check illegal move: Eating from outside, and not 3 consequitive
            elif piece.pos == (-1, -1):  # piece from outside
                countRow = 0
                countCol = 0
                countDiagonalL = 0
                countDiagonalR = 0
                # check legal row
                for i in range(4):
                    try:
                        if type(self.board.placement_on_board[row][i][-1]) == type(onBoard_piece[-1]):
                            countRow += 1
                    except IndexError as e:
                        # Handle IndexError (list index out of range)
                        pass
                # check legal column
                for i in range(4):
                    try:
                        if type(self.board.placement_on_board[i][col][-1]) == type(onBoard_piece[-1]):
                            countCol += 1
                    except IndexError as e:
                        pass
                # check legal diagonal left to right
                for i in range(4):
                    try:
                        if type(self.board.placement_on_board[i][i][-1]) == type(onBoard_piece[-1]):
                            countDiagonalL += 1
                    except IndexError as e:
                        pass
                # check legal diagonal right to left
                for i in range(4):
                    try:
                        if type(self.board.placement_on_board[i][3 - i][-1]) == type(onBoard_piece[-1]):
                            countDiagonalR += 1
                    except IndexError as e:
                        pass

                if countRow != 3 and countCol != 3 and countDiagonalR != 3 and countDiagonalL != 3:
                    return False
        
        return True

    def clone_board(self):
        # Create a deep copy of the board for generating new board states.
        # This ensures you don't alter the original board while simulating moves.
        # Create a new instance of Board
        res = Board()
        for whitePiece in self.board.whitePieces:
            newWhite = White((253, 187, 161),whitePiece.size,whitePiece.x,whitePiece.y)
            newWhite.pos = whitePiece.pos
            newWhite.isMovable = whitePiece.isMovable
            res.whitePieces.append(newWhite)
            if newWhite.pos != (-1,-1):
                res.placement_on_board[newWhite.pos[0]][newWhite.pos[1]].append(newWhite)
        for blackPiece in self.board.blackPieces:
            newBlack = Black((112, 57, 127), blackPiece.size, blackPiece.x, blackPiece.y)
            newBlack.pos = blackPiece.pos
            newBlack.isMovable = blackPiece.isMovable
            res.blackPieces.append(newBlack)
            if newBlack.pos != (-1,-1):
                res.placement_on_board[newBlack.pos[0]][newBlack.pos[1]].append(newBlack)
        
                    
        return res

