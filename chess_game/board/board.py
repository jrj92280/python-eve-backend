from chess_game.board.cell import Cell
from chess_game.pieces.bishop import Bishop
from chess_game.pieces.king import King
from chess_game.pieces.knight import Knight
from chess_game.pieces.pawn import Pawn
from chess_game.pieces.queen import Queen
from chess_game.pieces.rook import Rook


class Board:
    def __init__(self):
        board = []

        for row_index in range(1, 9):
            board_row = []

            for column_index in range(1, 9):
                cell = Cell(row_index, column_index)
                board_row.append(cell)

                if row_index == 2 or row_index == 7:
                    is_white = row_index == 2
                    pawn = Pawn(is_white=is_white)
                    cell.piece = pawn

            if row_index == 1 or row_index == 8:
                is_white = row_index == 1

                board_row[0].piece = Rook(is_white=is_white)
                board_row[1].piece = Knight(is_white=is_white)
                board_row[2].piece = Bishop(is_white=is_white)
                board_row[3].piece = King(is_white=is_white)
                board_row[4].piece = Queen(is_white=is_white)
                board_row[5].piece = Bishop(is_white=is_white)
                board_row[6].piece = Knight(is_white=is_white)
                board_row[7].piece = Rook(is_white=is_white)

            board.append(board_row)

        self.board = board

    @staticmethod
    def build_board(board_str: str) -> 'Board':
        board_rows = board_str.split('\n')

        game_board = []
        for row_index, board_row in enumerate(board_rows):
            cells = board_row.split(' ')

            row = []
            for cell_index, cell in enumerate(cells):
                row.append(Board._cell_factory(row_index, cell_index, cell))

            game_board.append(row)

        board = Board()
        board.board = game_board
        return board

    @staticmethod
    def _cell_factory(x: int, y: int, piece_str: str):
        is_white = True if piece_str[0] == 'w' else False
        piece_name = piece_str[1]
        has_moved = piece_str[2] == "1"

        piece = None
        if piece_name == 'p':
            piece = Pawn(is_white=is_white)
        elif piece_name == 'r':
            piece = Rook(is_white=is_white)
        elif piece_name == 'h':
            piece = Knight(is_white=is_white)
        elif piece_name == 'b':
            piece = Bishop(is_white=is_white)
        elif piece_name == 'k':
            piece = King(is_white=is_white)
        elif piece_name == 'q':
            piece = Queen(is_white=is_white)

        if piece:
            piece.has_moved = has_moved

        return Cell(x + 1, y + 1, piece, is_white=is_white)

    def __str__(self):
        board_str = '\n'.join(
            ' '.join([str(cell) if cell.piece else '###'
                      for cell in row])
            for row in self.board)
        return board_str
