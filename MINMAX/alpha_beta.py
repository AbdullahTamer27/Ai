import pygame
from Board import Board
from MINMAX.AI import get_all_movies
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
            _, move = alphabeta(position, depth, True, alpha, beta) # the alphabeta function returns alpha and best_move but we are interseted in the 2nd variable only
        else:
            _, move = alphabeta(position, depth, False, alpha, beta) # the alphabeta function returns beta and best_move but we are interseted in the 2nd variable only

        if move is not None:
            best_move = move
            best_evaluation = position.evaluate()

    return best_evaluation, best_move


def alphabeta (position, depth, max_player, alpha, beta):
    if depth == 0 or Board.checkWin():
        return position.evaluate(), position

    if max_player:
        best_move = None

        for move in get_all_movies(position, White ):
            evaluation = alphabeta(move, depth - 1, False, alpha, beta)
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

        for move in get_all_movies(position, Black, ):
            evaluation = alphabeta(move, depth - 1, True, alpha, beta)
            if (evaluation == -1):
                minval = beta
            else:
                minval = min(beta, evaluation)

            if(alpha >= minval):
                #cutoff
                beta = -1
                break
            else:
                beta = minval
            if beta == evaluation:
                best_move = move
        return beta, best_move
