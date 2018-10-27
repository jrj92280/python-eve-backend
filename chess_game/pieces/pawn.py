from chess_game.pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, *, is_white: bool = True):
        super().__init__('p', is_white=is_white)

    def hints(self, board):
        position = self.find_piece(board)
        hints = list()

        hints.append([position.x + 1, position.y])

        if position.x == 2:
            hints.append([position.x + 2, position.y])

        return hints
