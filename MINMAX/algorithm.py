import pygame
from Board import Board
from pieceGUI import White, Black
from MINMAX.AI import get_all_movies


def minimax (position, depth, max_player):
    if depth == 0 or Board.checkWin():
        return position.evaluate(), position

    if max_player:
        maxeval = float('-inf')
        best_move = None

        for move in get_all_movies(position, True ):
            evaluation = minimax(move, depth - 1, False)
            maxeval = max(maxeval, evaluation)
            if maxeval == evaluation:
                best_move = move
        return maxeval , best_move

    else:
        mineval = float('inf')
        best_move = None

        for move in get_all_movies(position, False ):
            evaluation = minimax(move, depth - 1, True)
            mineval = min(mineval, evaluation)
            if mineval == evaluation:
                best_move = move
        return mineval, best_move

