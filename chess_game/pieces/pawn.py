from chess_game.pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, *, is_white: bool = True):
        super().__init__('p', is_white=is_white)
