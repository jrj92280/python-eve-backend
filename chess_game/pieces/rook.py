from chess_game.pieces.piece import Piece


class Rook(Piece):
    def __init__(self, *, is_white: bool = True):
        super().__init__('r', is_white=is_white)

    def hints(self, board):
        position = self.find_piece(board)
        hints = list()

        allow_y_plus = True
        allow_y_minus = True
        allow_x_plus = True
        allow_x_minus = True

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

        if not self.has_moved:
            can_castle = True

            if position.y == 1:
                can_castle = self._is_open(position.x, 2, board)
                can_castle &= self._is_open(position.x, 3, board)
            if position.y == 8:
                can_castle = self._is_open(position.x, 7, board)
                can_castle &= self._is_open(position.x, 6, board)
                can_castle &= self._is_open(position.x, 5, board)

            king = board[position.x - 1][3].piece
            king = king and king.name == 'k'

            if can_castle and king:
                hints.append([position.x, 4])

        return hints
