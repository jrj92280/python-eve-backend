from chess_game.pieces.piece import Piece


class King(Piece):
    def __init__(self, *, is_white: bool = True):
        super().__init__('k', is_white=is_white)
