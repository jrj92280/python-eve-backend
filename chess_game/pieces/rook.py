from chess_game.pieces.piece import Piece


class Rook(Piece):
    def __init__(self, *, is_white: bool = True):
        super().__init__('r', is_white=is_white)

    def hints(self, board):
        position = self.find_piece(board)
        hints = list()

        return hints
