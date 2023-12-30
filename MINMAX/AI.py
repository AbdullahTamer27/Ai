from pieceGUI import Piece, White,Black
from Board import Board
class AI:
    def __init__(self, board):
        # self.placement_on_board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.board = board
    def all_moves(self, player):
        moves = []
        for row in range(4):
            for col in range(4):
                # Get the top piece on the current stack
                top_piece = self.board.placement_on_board[row][col][-1] if self.board.placement_on_board[row][col] else None

                # Generate all possible moves for 'player' from (row, col)
                if not top_piece or isinstance(top_piece, type(player)):  # Check if the current player can move here
                    for piece in self.get_player_pieces(player):
                        if self.can_move(piece, row, col):  # Ensure the move is legal
                            new_board = self.clone_board()  # Create a new board state
                            new_board.updatePlacement(row, col, piece)
                            moves.append(new_board)  # Add the new board state to moves list
                        for move in moves:
                            print(move.placement_on_board)
                        print('---------------------------------------------')


        return moves

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
            # OnBoard Piece is Big
            if onBoard_piece[-1].size >= piece.size:
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
        res.placement_on_board = []
        for whitePiece in self.board.whitePieces:
            res.whitePieces.append(whitePiece)
        for blackPiece in self.board.blackPieces:
            res.blackPieces.append(blackPiece)
        res.placement_on_board = [[list(stack) for stack in row] for row in self.board.placement_on_board]
        return res

