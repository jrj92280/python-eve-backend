class Piece:
    def __init__(self, name, *, is_white: bool = True):
        self.name = name
        self.is_white = is_white
        self.color = 'white' if is_white else 'black'
        self.has_moved = False

    def find_piece(self, board):
        position = None
        for row in board:
            for cell in row:
                if cell.piece == self:
                    position = cell
        return position

    @property
    def image(self):
        return str(self)[:2]

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

    def __str__(self):
        move_indicator = 1 if self.has_moved else 0
        return f'{self.color[0]}{self.name}{move_indicator}'
