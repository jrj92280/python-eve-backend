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

# 
# def test_move(board):
#     expected_hints = [[4, 2]]
#     rook = board.board[2][1].piece
# 
#     hints = rook.hints(board.board)
# 
#     assert expected_hints == hints
#
#
# def test_move_black(board):
#     expected_hints = [[5, 7]]
#     rook = board.board[5][6].piece
#
#     hints = rook.hints(board.board)
#
#     assert expected_hints == hints
#
#
# def test_blocked(board):
#     expected_hints = []
#     rook = board.board[1][7].piece
#
#     hints = rook.hints(board.board)
#
#     assert expected_hints == hints
#
#
# def test_blocked_black(board):
#     expected_hints = []
#     rook = board.board[4][3].piece
#
#     hints = rook.hints(board.board)
#
#     assert expected_hints == hints
#
#
# def test_attack(board):
#     expected_hints = [[5, 5]]
#     rook = board.board[3][3].piece
#
#     hints = rook.hints(board.board)
#
#     assert expected_hints == hints
#
#
# def test_attack_black(board):
#     expected_hints = [[2, 5], [2, 7]]
#     rook = board.board[2][5].piece
#
#     hints = rook.hints(board.board)
#
#     assert expected_hints == hints
