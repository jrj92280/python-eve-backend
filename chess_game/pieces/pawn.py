from chess_game.pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, *, is_white: bool = True):
        super().__init__('p', is_white=is_white)

    def hints(self, board):
        position = self.find_piece(board)
        hints = list()

        move_direction = 1 if self.is_white else -1

        self._append_hint_if_valid(position.x + (1 * move_direction), position.y, board, hints, can_attack=False)

        if not self.has_moved and self._is_open(position.x + (1 * move_direction), position.y, board):
            self._append_hint_if_valid(position.x + (2 * move_direction), position.y, board, hints, can_attack=False)

        attacks = self.attacks(board)
        hints.extend(attacks)
        return hints

    def attacks(self, board, *, is_check_threats=False):
        position = self.find_piece(board)
        attacks = list()

        move_direction = 1 if self.is_white else -1

        if self._is_enemy(position.x + (1 * move_direction), position.y - 1, board) or is_check_threats:
            self._append_hint_if_valid(position.x + (1 * move_direction), position.y - 1, board, attacks)

        if self._is_enemy(position.x + (1 * move_direction), position.y + 1, board) or is_check_threats:
            self._append_hint_if_valid(position.x + (1 * move_direction), position.y + 1, board, attacks)

        return attacks
