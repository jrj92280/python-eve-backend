from chess_game.pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, *, is_white: bool = True):
        super().__init__('p', is_white=is_white)

    def hints(self, board):
        position = self.find_piece(board)
        hints = list()

        self._append_hint_if_valid(position.x + 1, position.y, board, hints, can_attack=False)

        if position.x == 2 and self._is_open(position.x + 1, position.y, board):
            self._append_hint_if_valid(position.x + 2, position.y, board, hints, can_attack=False)

        if self._is_enemy(position.x + 1, position.y - 1, board):
            self._append_hint_if_valid(position.x + 1, position.y - 1, board, hints)

        if self._is_enemy(position.x + 1, position.y + 1, board):
            self._append_hint_if_valid(position.x + 1, position.y + 1, board, hints)

        return hints

    @staticmethod
    def _is_valid_position(position_x, position_y, board):
        index_x = position_x - 1
        index_y = position_y - 1

        return 0 <= index_x < len(board) and 0 <= index_y < len(board[index_x])

    def _append_hint_if_valid(self, position_x, position_y, board, hints, *, can_attack=True):
        if self._is_valid_position(position_x, position_y, board) and \
                (self._is_open(position_x, position_y, board) or (
                        can_attack and self._is_enemy(position_x, position_y, board))):
            hints.append([position_x, position_y])

    def _is_open(self, position_x, position_y, board):
        index_x = position_x - 1
        index_y = position_y - 1

        return self._is_valid_position(position_x, position_y, board) and not board[index_x][index_y].piece

    def _is_enemy(self, position_x, position_y, board):
        index_x = position_x - 1
        index_y = position_y - 1

        if not self._is_valid_position(position_x, position_y, board):
            return False

        piece = board[index_x][index_y].piece
        return piece and not piece.color == self.color
