import pytest

from chess_game.board.board import Board
from chess_game.pieces.bishop import Bishop
from test.utils import assert_lists_equivalent


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
    br bh bb bk bq bb bh br
    """
    return board


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
