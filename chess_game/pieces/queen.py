from chess_game.pieces.piece import Piece


class Queen(Piece):
    def __init__(self, *, is_white: bool = True):
        super().__init__('q', is_white=is_white)
