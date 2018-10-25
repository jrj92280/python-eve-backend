class Piece:
    def __init__(self, *, is_white: bool = True):
        self.color = 'white' if is_white else 'black'
