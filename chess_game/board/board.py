from chess_game.board.cell import Cell
from chess_game.pieces.pawn import Pawn


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

            board.append(board_row)

        # white_pieces = ["WR", "WH", "WB", "WK", "WQ", "WB", "WH", "WR"]
        # game_board[0] = white_pieces
        #
        # black_pieces = ["BR", "BH", "BB", "BQ", "BK", "BB", "BH", "BR"]
        # game_board[7] = black_pieces
        # # print("\n".join([str(row) for row in game_board]))

        self.board = board
