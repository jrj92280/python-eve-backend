from chess_game.pieces.piece import Piece


class Cell:
    def __init__(self, x: int, y: int, piece: Piece = None, *, is_white: bool = True):
        self.x = x
        self.y = y
        self.color = 'white' if is_white else 'black'
        self.piece = piece

    def __str__(self):
        piece_name = str(self.piece) if self.piece else ''
        return piece_name
