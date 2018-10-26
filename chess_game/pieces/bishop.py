from chess_game.pieces.piece import Piece


class Bishop(Piece):
    def __init__(self, *, is_white: bool = True):
        super().__init__('b', is_white=is_white)
