import pytest

from chess_game.board.board import Board
from chess_game.pieces.rook import Rook


@pytest.fixture
def board():
    board = Board()

    board.board[0][7].piece = None
    board.board[4][4].piece = Rook()

    board.board[7][1].piece = None
    board.board[7][2].piece = None
    board.board[7][3].piece = None
    board.board[7][5].piece = None
    board.board[7][6].piece = None

    """ board
    wr wh wb wk wq wb wh ##
    wp wp wp wp wp wp wp wp
    ## ## ## ## ## ## ## ##
    ## ## ## ## ## ## ## ##
    ## ## ## ## wr ## ## ##
    ## ## ## ## ## ## ## ##
    bp bp bp bp bp bp bp bp
    br ## ## ## bk ## ## br
    """
    return board


def assert_lists_equivalent(expected, actual):
    for item in expected:
        assert item in actual

    for item in actual:
        assert item in expected


def test_blocked(board):
    expected_hints = []
    rook = board.board[0][0].piece

    hints = rook.hints(board.board)

    assert expected_hints == hints


def test_move(board):
    expected_hints = [[3, 5], [4, 5], [6, 5], [7, 5], [5, 1], [5, 2], [5, 3], [5, 4], [5, 6], [5, 7], [5, 8]]
    rook = board.board[4][4].piece

    hints = rook.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)


def test_castle_bottom_left(board):
    expected_hints = [[8, 2], [8, 3], [8, 4], [8, 5]]
    rook = board.board[7][0].piece

    hints = rook.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)


def test_castle_bottom_right(board):
    expected_hints = [[8, 7], [8, 6], [8, 5]]
    rook = board.board[7][7].piece

    hints = rook.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)


def test_castle_top():
    board = Board()

    board.board[0][1].piece = None
    board.board[0][2].piece = None
    board.board[0][4].piece = None
    board.board[0][5].piece = None
    board.board[0][6].piece = None

    """ board
    wr ## ## wk ## ## ## wr
    wp wp wp wp wp wp wp wp
    ## ## ## ## ## ## ## ##
    ## ## ## ## ## ## ## ##
    ## ## ## ## ## ## ## ##
    ## ## ## ## ## ## ## ##
    bp bp bp bp bp bp bp bp
    br bh bb bq bk bb bh br
    """

    # top left
    expected_hints = [[1, 2], [1, 3], [1, 4]]
    rook = board.board[0][0].piece

    hints = rook.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)

    # top right
    expected_hints = [[1, 4], [1, 5], [1, 6], [1, 7]]
    rook = board.board[0][7].piece

    hints = rook.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)