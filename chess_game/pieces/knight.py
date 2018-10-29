from chess_game.pieces.piece import Piece


class Knight(Piece):
    def __init__(self, *, is_white: bool = True):
        super().__init__('h', is_white=is_white)

    def hints(self, board):
        pass
