import pytest

from chess_game.board.board import Board
from chess_game.pieces.rook import Rook
from test.utils import assert_lists_equivalent


@pytest.fixture
def board():
    board = Board()

    board.board[0][7].piece = None
    board.board[4][4].piece = Rook()

    board.board[7][1].piece = None
    board.board[7][2].piece = None
    board.board[7][4].piece = None
    board.board[7][5].piece = None
    board.board[7][6].piece = None

    """ board
    wr0 wh0 wb0 wk0 wq0 wb0 wh0 ###
    wp0 wp0 wp0 wp0 wp0 wp0 wp0 wp0
    ### ### ### ### ### ### ### ###
    ### ### ### ### ### ### ### ###
    ### ### ### ### wr0 ### ### ###
    ### ### ### ### ### ### ### ###
    bp0 bp0 bp0 bp0 bp0 bp0 bp0 bp0
    br0 ### ### bk0 ### ### ### br0
    """

    return board


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
    expected_hints = [[8, 2], [8, 3], [8, 4]]
    rook = board.board[7][0].piece

    hints = rook.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)


def test_castle_bottom_right(board):
    expected_hints = [[8, 7], [8, 6], [8, 5], [8, 4]]

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

    board.board[7][0].piece.has_moved = True
    board.board[7][1].piece = None
    board.board[7][2].piece = None
    board.board[7][4].piece = None
    board.board[7][5].piece = None
    board.board[7][6].piece = None
    board.board[7][7].piece.has_moved = True

    """ board
    wr0 ### ### wk0 ### ### ### wr0
    wp0 wp0 wp0 wp0 wp0 wp0 wp0 wp0
    ### ### ### ### ### ### ### ###
    ### ### ### ### ### ### ### ###
    ### ### ### ### ### ### ### ###
    ### ### ### ### ### ### ### ###
    bp0 bp0 bp0 bp0 bp0 bp0 bp0 bp0
    br1 ### ### bk0 ### ### ### br1
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

    # bottom left
    expected_hints = [[8, 2], [8, 3]]
    rook = board.board[7][0].piece

    hints = rook.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)

    # bottom right
    expected_hints = [[8, 5], [8, 6], [8, 7]]
    rook = board.board[7][7].piece

    hints = rook.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)

    board.board[7][0].piece.has_moved = False
    board.board[7][7].piece.has_moved = False
    board.board[7][3].piece.has_moved = True  # king


def test_cant_castle_king_move():
    board = Board()

    board.board[7][3].piece.has_moved = True

    board.board[7][1].piece = None
    board.board[7][2].piece = None
    board.board[7][4].piece = None
    board.board[7][5].piece = None
    board.board[7][6].piece = None

    """ board
    wr0 wh0 wb0 wk0 wq0 wb0 wh0 wr0
    wp0 wp0 wp0 wp0 wp0 wp0 wp0 wp0
    ### ### ### ### ### ### ### ###
    ### ### ### ### ### ### ### ###
    ### ### ### ### ### ### ### ###
    ### ### ### ### ### ### ### ###
    bp0 bp0 bp0 bp0 bp0 bp0 bp0 bp0
    br0 ### ### bk1 ### ### ### br0
    """

    expected_hints = [[8, 5], [8, 6], [8, 7]]
    rook = board.board[7][7].piece

    hints = rook.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)
