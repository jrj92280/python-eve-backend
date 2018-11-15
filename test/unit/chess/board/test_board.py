from chess_game.models.board import Board


def test_board_init():
    board = Board()
    assert 8 == len(board.board)
    for row in board.board:
        assert 8 == len(row)


def test_game_board_has_pawns():
    board = Board()

    board_white_pawn_row = board.board[1]
    for cell in board_white_pawn_row:
        assert 'wp0' == str(cell)

    board_black_pawn_row = board.board[6]
    for cell in board_black_pawn_row:
        assert 'bp0' == str(cell)


def test_game_board_has_empty_spaces():
    board = Board()

    for row in range(2, 6):
        board_row = board.board[row]
        for cell in board_row:
            assert '' == str(cell)


def test_game_board_has_white_pieces():
    expected_white_pieces = ["wr0", "wh0", "wb0", "wk0", "wq0", "wb0", "wh0", "wr0"]

    board = Board()
    white_row = board.board[0]

    for index, cell in enumerate(white_row):
        assert str(cell) == expected_white_pieces[index]


def test_game_board_has_black_pieces():
    expected_black_pieces = ["br0", "bh0", "bb0", "bk0", "bq0", "bb0", "bh0", "br0"]

    board = Board()
    black_row = board.board[7]

    for index, cell in enumerate(black_row):
        assert str(cell) == expected_black_pieces[index]
