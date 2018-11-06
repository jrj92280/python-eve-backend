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

    def __str__(self):
        board_str = '\n'.join(
            ' '.join([str(cell) if cell.piece else '##'
                      for cell in row])
            for row in self.board)
        return board_str
