import pygame
from Board import Board
from MINMAX.AI import get_all_movies
from pieceGUI import White, Black



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
