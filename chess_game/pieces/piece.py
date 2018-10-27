class Piece:
    def __init__(self, name, *, is_white: bool = True):
        self.name = name
        self.color = 'white' if is_white else 'black'

    def find_piece(self, board):
        position = None
        for row in board:
            for cell in row:
                if cell.piece == self:
                    position = cell
        return position

    def __str__(self):
        return f'{self.color[0]}{self.name}'
