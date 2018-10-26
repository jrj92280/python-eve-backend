class Piece:
    def __init__(self, name, *, is_white: bool = True):
        self.name = name
        self.color = 'white' if is_white else 'black'

    def __str__(self):
        return f'{self.color[0]}{self.name}'

    def __eq__(self, other):
        return str(self) == str(other)
