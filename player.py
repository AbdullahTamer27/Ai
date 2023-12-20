from piece import Piece
class Player:
    def __init__(self, color):
        self.color = color
        self.pieces = [Piece(color) for _ in range(12)]
