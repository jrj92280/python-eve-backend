from chess_game.pieces.piece import Piece


class Knight(Piece):
    def __init__(self, *, is_white: bool = True):
        super().__init__('h', is_white=is_white)

    def hints(self, board):
        position = self.find_piece(board)
        hints = list()

        self._append_hint_if_valid(position.x + 2, position.y + 1, board, hints)
        self._append_hint_if_valid(position.x + 2, position.y - 1, board, hints)

        self._append_hint_if_valid(position.x - 2, position.y + 1, board, hints)
        self._append_hint_if_valid(position.x - 2, position.y - 1, board, hints)

        self._append_hint_if_valid(position.x + 1, position.y + 2, board, hints)
        self._append_hint_if_valid(position.x - 1, position.y + 2, board, hints)

        self._append_hint_if_valid(position.x + 1, position.y - 2, board, hints)
        self._append_hint_if_valid(position.x - 1, position.y - 2, board, hints)

        return hints
