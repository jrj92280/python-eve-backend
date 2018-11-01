import pytest

from chess_game.board.board import Board
from chess_game.pieces.bishop import Bishop


@pytest.fixture
def board():
    board = Board()

    board.board[0][5].piece = None
    board.board[4][4].piece = Bishop()

    """ board
    wr wh wb wk wq ## wh wr
    wp wp wp wp wp wp wp wp
    ## ## ## ## ## ## ## ##
    ## ## ## ## ## ## ## ##
    ## ## ## ## wb ## ## ##
    ## ## ## ## ## ## ## ##
    bp bp bp bp bp bp bp bp
    br bh bb bq bk bb bh br
    """
    return board


def assert_lists_equivalent(expected, actual):
    for item in expected:
        assert item in actual

    for item in actual:
        assert item in expected


def test_blocked(board):
    expected_hints = []
    bishop = board.board[0][2].piece

    hints = bishop.hints(board.board)

    assert expected_hints == hints


def test_move(board):
    expected_hints = [[4, 4], [3, 3],
                      [4, 6], [3, 7],
                      [6, 4], [7, 3],
                      [6, 6], [7, 7]]

    bishop = board.board[4][4].piece

    hints = bishop.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)
