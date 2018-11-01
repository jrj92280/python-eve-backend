from chess_game.pieces.piece import Piece


class Queen(Piece):
    def __init__(self, *, is_white: bool = True):
        super().__init__('q', is_white=is_white)

    def hints(self, board):
        position = self.find_piece(board)
        hints = list()

        allow_y_plus = True
        allow_y_minus = True
        allow_x_plus = True
        allow_x_minus = True

        allow_y_plus_x_plus = True
        allow_x_plus_y_minus = True
        allow_x_minus_y_plus = True
        allow_x_minus_y_minus = True

        for index in range(1, 8):
            if allow_y_plus:
                allow_y_plus = self._is_open(position.x, position.y + index, board)
                self._append_hint_if_valid(position.x, position.y + index, board, hints)
            if allow_y_minus:
                allow_y_minus = self._is_open(position.x, position.y - index, board)
                self._append_hint_if_valid(position.x, position.y - index, board, hints)
            if allow_x_plus:
                allow_x_plus = self._is_open(position.x + index, position.y, board)
                self._append_hint_if_valid(position.x + index, position.y, board, hints)
            if allow_x_minus:
                allow_x_minus = self._is_open(position.x - index, position.y, board)
                self._append_hint_if_valid(position.x - index, position.y, board, hints)

            if allow_y_plus_x_plus:
                allow_y_plus_x_plus = self._is_open(position.x + index, position.y + index, board)
                self._append_hint_if_valid(position.x + index, position.y + index, board, hints)
            if allow_x_plus_y_minus:
                allow_x_plus_y_minus = self._is_open(position.x + index, position.y - index, board)
                self._append_hint_if_valid(position.x + index, position.y - index, board, hints)
            if allow_x_minus_y_plus:
                allow_x_minus_y_plus = self._is_open(position.x - index, position.y + index, board)
                self._append_hint_if_valid(position.x - index, position.y + index, board, hints)
            if allow_x_minus_y_minus:
                allow_x_minus_y_minus = self._is_open(position.x - index, position.y - index, board)
                self._append_hint_if_valid(position.x - index, position.y - index, board, hints)

        return hints
