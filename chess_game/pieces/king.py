from chess_game.pieces.piece import Piece


class King(Piece):
    def __init__(self, *, is_white: bool = True):
        super().__init__('k', is_white=is_white)

    def hints(self, board):
        position = self.find_piece(board)
        hints = list()

        self._append_hint_if_valid(position.x, position.y + 1, board, hints)
        self._append_hint_if_valid(position.x, position.y - 1, board, hints)
        self._append_hint_if_valid(position.x + 1, position.y, board, hints)
        self._append_hint_if_valid(position.x - 1, position.y, board, hints)
        self._append_hint_if_valid(position.x + 1, position.y + 1, board, hints)
        self._append_hint_if_valid(position.x + 1, position.y - 1, board, hints)
        self._append_hint_if_valid(position.x - 1, position.y + 1, board, hints)
        self._append_hint_if_valid(position.x - 1, position.y - 1, board, hints)

        # threats = self.threats(board)
        #
        # _hints = []
        # for hint in hints:
        #     if hint in threats:
        #         continue
        #     _hints.append(hint)

        return hints

    def threats(self, board):
        threats = []
        for row in board:
            for column in row:
                piece = column.piece
                if not piece:
                    continue
                if piece.is_white == self.is_white:
                    continue
                threats.extend(piece.hints(board))
        return threats
