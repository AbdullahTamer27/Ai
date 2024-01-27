import pygame
from Board import Board
from pieceGUI import White, Black
import time



def iterative_deepening_alphabeta(position, max_player, max_depth, time_limit):
    start_time = time.time() #Records The Start Time 
    best_move = None #To Record the best move after each iteration so when time ends we return the last saced value
    best_evaluation = None #To Record the best evaluation after each iteration so when time ends we return the last saced value

    for depth in range(1, max_depth + 1): # we gonna iterate from the start depth to the max_depth based as a paremter
        #3dad el iterations = the depth you want to reach  by the end of the final iteration
        #each time the depth value increase untill it reaches max depth
        #at the begining of each iteration hnsfr el alpha wel beta 
        alpha = float('-inf')
        beta = float('inf')

        elapsed_time = time.time() - start_time #Calculate the  time taken  since the start of the search.
        if elapsed_time > time_limit:
            break  # Exit loop if time limit exceeded

        if max_player:
            time_remaining = time_limit - elapsed_time
            test = alphabeta_timelimit(position, depth, True, alpha, beta, time_remaining) # the alphabeta function returns alpha and best_move but we are interseted in the 2nd variable only

        else:
            test = alphabeta_timelimit(position, depth, False, alpha, beta, time_remaining) # the alphabeta function returns beta and best_move but we are interseted in the 2nd variable only

        if test is None:
            move = None
        else:
            move = test[1]
        if move is not None:
            best_move = move
            best_evaluation = position.evaluate(max_player) # the value of desirability if max player the max value is returned , if min player the min value is returned

    return best_evaluation, best_move

def alphabeta_timelimit (board, depth, max_player, alpha, beta,timelimit):
    start_time = time.time()
    if timelimit <= 0:
        return None
    position = board
    cloned = Board()
    cloned = clone_board(board)
    if depth == 0:
        return position.evaluate(max_player), position

    if max_player:
        best_move = None
        for moves in get_all_moves(cloned, not max_player ):
            for move in moves:
                elapsed_time = time.time() - start_time 
                time_remaining = timelimit - elapsed_time
                test = alphabeta_timelimit(move, depth - 1, False, alpha, beta,time_remaining)
                if test is None:
                    return None
                evaluation = test[0]
                if (evaluation == -1):
                    maxval = alpha
                else:
                    maxval = max(alpha, evaluation)
                if (maxval >= beta):
                    #cutoff
                    alpha = -1
                    break
                else:
                    alpha = maxval
                if alpha == evaluation:
                    best_move = move
        return alpha , best_move

    else:
        best_move = None

        for moves in get_all_moves(cloned, not max_player ):
            for move in moves:
                elapsed_time = time.time() - start_time 
                time_remaining = timelimit - elapsed_time
                test = alphabeta_timelimit(move, depth - 1, True, alpha, beta,time_remaining)
                if test is None:
                    return None
                evaluation = test[0]
                if (evaluation == -1):
                    minval = beta
                else:
                    minval =  min(beta, evaluation)

                if(alpha >= minval):
                    #cutoff
                    beta = -1
                    break
                else:
                    beta = minval
                if beta == evaluation:
                    best_move = move
        return beta, best_move

def alphabeta (board, depth, max_player, alpha, beta):
    position = board
    cloned = Board()
    cloned = clone_board(board)
    if depth == 0:
        return position.evaluate(max_player), position

    if max_player:
        best_move = None
        for moves in get_all_moves(cloned, not max_player ):
            for move in moves:
                (evaluation, x) = alphabeta(move, depth - 1, False, alpha, beta)
                if (evaluation == -1):
                    maxval = alpha
                else:
                    maxval = max(alpha, evaluation)
                if (maxval >= beta):
                    #cutoff
                    alpha = -1
                    break
                else:
                    alpha = maxval
                if alpha == evaluation:
                    best_move = move
        return alpha , best_move

    else:
        best_move = None

        for moves in get_all_moves(cloned, not max_player ):
            for move in moves:
                (evaluation, x) = alphabeta(move, depth - 1, True, alpha, beta)
                if (evaluation == -1):
                    minval = beta
                else:
                    minval =  min(beta, evaluation)

                if(alpha >= minval):
                    #cutoff
                    beta = -1
                    break
                else:
                    beta = minval
                if beta == evaluation:
                    best_move = move
        return beta, best_move

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