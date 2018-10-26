from chess_game.pieces.piece import Piece


class Rook(Piece):
    def __init__(self, *, is_white: bool = True):
        super().__init__('r', is_white=is_white)
