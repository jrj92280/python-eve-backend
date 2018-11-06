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


def test_game_board_has_white_pieces():
    expected_white_pieces = ["wr", "wh", "wb", "wk", "wq", "wb", "wh", "wr"]

    board = Board()
    white_row = board.board[0]

    for index, cell in enumerate(white_row):
        assert str(cell) == expected_white_pieces[index]


def test_game_board_has_black_pieces():
    expected_black_pieces = ["br", "bh", "bb", "bk", "bq", "bb", "bh", "br"]

    board = Board()
    black_row = board.board[7]

    for index, cell in enumerate(black_row):
        assert str(cell) == expected_black_pieces[index]
