import pygame
from Board import Board
from pieceGUI import White, Black


# max_player: bool , TRUE WHITE, FALSE BLACK
def minimax (board, depth, max_player):
    position = board
    cloned = Board()
    cloned = clone_board(board)
    print(depth)
    print("current board: ", board.printBoard())
    #print("current clonedboard: ", cloned.printBoard())
    if depth == 0: #check later or position.checkWin()
        return position.evaluate(max_player), position

    if max_player:
        maxeval = float('-inf')
        best_move = None

        for moves in get_all_moves(cloned, not max_player ): # TRUE = white
            for move in moves:
                #print("move in max: ", move.printBoard())
                clonedmove = clone_board(move)
                #print("clonedmove in max: ", clonedmove.printBoard())
                #print("move in should be equal to move: ", Ai.board.printBoard())
                (evaluation, x) = minimax(move, depth - 1, False)
                #Ai.board = temp
                maxeval = max(maxeval, evaluation)
                # print("maxeval after min: ", maxeval)
                print("max current board: ", move.printBoard())
                if maxeval == evaluation:
                    best_move = move
        return maxeval , best_move

    else:
        mineval = float('inf')
        best_move = None
        
        for moves in get_all_moves(cloned, not max_player ):
            for move in moves:
                #print("move in min: ", move.printBoard())
                clonedmove = clone_board(move)
                #print("clonedmove in min: ", clonedmove.printBoard())
                #temp = Ai.board
                (evaluation, x) = minimax(move, depth - 1, True)
                #Ai.board = temp
                #print("mineval: ", mineval, "evaluation: ", evaluation)
                mineval = min(mineval, evaluation)
                # print("mineval after min: ", mineval)
                print("min current board: ", move.printBoard())
                if mineval == evaluation:
                    best_move = move
        return mineval, best_move


def testsimulation(board):
    
    print("Input board: " ,board.printBoard())
    moves = get_all_moves(board,False)
    for move in moves[0]:
        print("move1: ", move.printBoard())
        
        for moves2 in get_all_moves(move, True):
            for move2 in moves2:
                print("move2: ", move2.printBoard())
                '''
                for moves3 in get_all_moves(move2, False):
                    for move3 in moves3:
                        print("move3: " ,move3.printBoard())
                    
                        for moves4 in get_all_moves(move3, True):
                            for move4 in moves4:
                                print("move4: " ,move4.printBoard())
                                break
                '''
    return
def clone_simulated_board(board):
    return

def compare(old_board, new_board):
    new_pos= (-1,-1)
    # for new_white in new_board.whitePieces:
    #     for old_white in old_board.whitePieces:
    #         if new_white.idx == old_white.idx:
    #             if new_white.pos != old_white.pos:
    #                 new_pos = new_white.pos
    #                 if new_pos == (None, None):
    #                     continue
    #                 print("old_white id: ", old_white.idx, "new_pos: ", new_pos)
    #                 if old_white is not None:
    #                     return old_white, new_pos
    for new_black in new_board.blackPieces:
        for old_black in old_board.blackPieces:
            if new_black.idx == old_black.idx:
                if new_black.pos != old_black.pos:
                    new_pos = new_black.pos
                    if new_pos == (None, None):
                        continue
                    print("old_black id: ", old_black.idx, "new_pos: ", new_pos)
                    if old_black is not None:
                        if new_pos is not None:
                            return old_black, new_pos
    #return piece, pos
def compare_white(old_board, new_board):
    new_pos= (-1,-1)
    for new_white in new_board.whitePieces:
        for old_white in old_board.whitePieces:
            if new_white.idx == old_white.idx:
                if new_white.pos != old_white.pos:
                    new_pos = new_white.pos
                    if new_pos == (None, None):
                        continue
                    print("old_white id: ", old_white.idx, "new_pos: ", new_pos)
                    if old_white is not None:
                        return old_white, new_pos
    #return piece, pos
def clone_board(board):
    res = Board()

    for whitePiece in board.whitePieces:
        newWhite = White((253, 187, 161), whitePiece.size, whitePiece.x, whitePiece.y)
        newWhite.pos = whitePiece.pos
        newWhite.idx = whitePiece.idx
        newWhite.isMovable = whitePiece.isMovable
        res.whitePieces.append(newWhite)

        if newWhite.pos != (None, None):
            res.placement_on_board[newWhite.pos[0]][newWhite.pos[1]].append(newWhite)

    for blackPiece in board.blackPieces:
        newBlack = Black((112, 57, 127), blackPiece.size, blackPiece.x, blackPiece.y)
        newBlack.pos = blackPiece.pos
        newBlack.idx = blackPiece.idx
        newBlack.isMovable = blackPiece.isMovable
        res.blackPieces.append(newBlack)

        if newBlack.pos != (None, None):
            res.placement_on_board[newBlack.pos[0]][newBlack.pos[1]].append(newBlack)

    return res


def all_moves(board, piece):
        #print(piece.idx, piece.size)
        
        # playerturn = true then white turn
        # playerturn = false then black turn
        moves = []
        for row in range(4):
            for col in range(4):
                if can_move(board,piece, row, col):  # Ensure the move is legal
                    new_board = clone_board(board)  # Create a new board state
                    test = new_board.simulatePlacement(row, col, piece)
                    if test:
                        #new_board.updatePlacement(row, col, piece)
                        for black in new_board.blackPieces:
                            if black.idx == piece.idx:
                                new_board.placement_on_board[row][col].append(black)
                                black.setPos((row,col))
                        for white in new_board.whitePieces:
                            if white.idx == piece.idx:
                                new_board.placement_on_board[row][col].append(white)
                                white.setPos((row,col))
                        #piece.setPos((row,col))
                    moves.append(new_board)  
                    # Add the new board state to moves list
        # for move in moves:
        #     for row in move.placement_on_board:
        #         print(row)
            # print(move.printBoard())
        # print('\n\n---------------------------------------------\n\n')
        return moves


def get_all_moves(board, playerturn):
        new_board = clone_board(board)
        output = []
        if playerturn: 
            for whitePiece in new_board.whitePieces:
                if whitePiece.isMovable:
                     output.append(all_moves(board,whitePiece))

        elif not playerturn:
            for blackPiece in new_board.blackPieces:
                if blackPiece.isMovable:
                     output.append(all_moves(board, blackPiece))
        return output

    
def can_move(board, piece, row, col):
    # Determine if 'piece' can legally move to (row, col) on the current board.
    # Include logic for checking if the piece can gobble, move into an empty space, etc.
    onBoard_piece = board.placement_on_board[row][col]
    
    if onBoard_piece:
        if onBoard_piece[-1] == piece:
            return True
        # OnBoard Piece is Big
        if onBoard_piece[-1].size >= piece.size and id(piece) != id(onBoard_piece[-1]):
            return False
        # OnBoard Piece not big
        # Check illegal move: Eating from outside, and not 3 consequitive
        elif piece.pos == (None, None):  # piece from outside
            countRow = 0
            countCol = 0
            countDiagonalL = 0
            countDiagonalR = 0
            # check legal row
            for i in range(4):
                try:
                    if type(board.placement_on_board[row][i][-1]) == type(onBoard_piece[-1]):
                        countRow += 1
                except IndexError as e:
                    # Handle IndexError (list index out of range)
                    pass
            # check legal column
            for i in range(4):
                try:
                    if type(board.placement_on_board[i][col][-1]) == type(onBoard_piece[-1]):
                        countCol += 1
                except IndexError as e:
                    pass
            # check legal diagonal left to right
            for i in range(4):
                try:
                    if type(board.placement_on_board[i][i][-1]) == type(onBoard_piece[-1]):
                        countDiagonalL += 1
                except IndexError as e:
                    pass
            # check legal diagonal right to left
            for i in range(4):
                try:
                    if type(board.placement_on_board[i][3 - i][-1]) == type(onBoard_piece[-1]):
                        countDiagonalR += 1
                except IndexError as e:
                    pass

            if countRow != 3 and countCol != 3 and countDiagonalR != 3 and countDiagonalL != 3:
                return False
    
    return True



def minimax_easy (board, depth, max_player):
    position = board
    cloned = Board()
    cloned = clone_board(board)
    print(depth)
    print("current board: ", board.printBoard())
    #print("current clonedboard: ", cloned.printBoard())
    if depth == 0: #check later or position.checkWin()
        return position.evaluate_easy(max_player), position

    if max_player:
        maxeval = float('-inf')
        best_move = None

        for moves in get_all_moves(cloned, not max_player ): # TRUE = white
            for move in moves:
                #print("move in max: ", move.printBoard())
                clonedmove = clone_board(move)
                #print("clonedmove in max: ", clonedmove.printBoard())
                #print("move in should be equal to move: ", Ai.board.printBoard())
                (evaluation, x) = minimax(move, depth - 1, False)
                #Ai.board = temp
                maxeval = max(maxeval, evaluation)
                # print("maxeval after min: ", maxeval)
                print("max current board: ", move.printBoard())
                if maxeval == evaluation:
                    best_move = move
        return maxeval , best_move

    else:
        mineval = float('inf')
        best_move = None
        
        for moves in get_all_moves(cloned, not max_player ):
            for move in moves:
                #print("move in min: ", move.printBoard())
                clonedmove = clone_board(move)
                #print("clonedmove in min: ", clonedmove.printBoard())
                #temp = Ai.board
                (evaluation, x) = minimax(move, depth - 1, True)
                #Ai.board = temp
                #print("mineval: ", mineval, "evaluation: ", evaluation)
                mineval = min(mineval, evaluation)
                # print("mineval after min: ", mineval)
                print("min current board: ", move.printBoard())
                if mineval == evaluation:
                    best_move = move
        return mineval, best_move