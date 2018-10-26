from chess_game.board.board import Board


def test_board_init():
    board = Board()
    assert 8 == len(board.board)
    for row in board.board:
        assert 8 == len(row)


def test_game_board_has_pawns():
    board = Board()

    board_white_pawn_row = board.board[1]
    for cell in board_white_pawn_row:
        assert 'wp' == str(cell)

    board_black_pawn_row = board.board[6]
    for cell in board_black_pawn_row:
        assert 'bp' == str(cell)


def test_game_board_has_empty_spaces():
    board = Board()

    for row in range(2, 6):
        board_row = board.board[row]
        for cell in board_row:
            assert '' == str(cell)

# def test_game_board_has_white_pieces():
#     white_pieces = ["WR", "WH", "WB", "WK", "WQ", "WB", "WH", "WR"]
#
#     board = make_board()
#
#     assert white_pieces == board[0]
#
#
# def test_game_board_has_black_pieces():
#     black_pieces = ["BR", "BH", "BB", "BQ", "BK", "BB", "BH", "BR"]
#
#     board = make_board()
#
#     assert black_pieces == board[7]
