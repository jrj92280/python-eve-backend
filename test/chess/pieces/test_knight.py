import pytest

from chess_game.board.board import Board
from chess_game.pieces.knight import Knight
from test.utils import assert_lists_equivalent


@pytest.fixture
def board():
    board = Board()

    board.board[0][1].piece = None
    board.board[4][3].piece = Knight()

    """ board
    wr ## wb wk wq wb wh wr
    wp wp wp wp wp wp wp wp
    ## ## ## ## ## ## ## ##
    ## ## ## ## ## ## ## ##
    ## ## ## wh ## ## ## ##
    ## ## ## ## ## ## ## ##
    bp bp bp bp bp bp bp bp
    br bh bb bq bk bb bh br
    """
    return board


def test_blocked(board):
    expected_hints = [[3, 6], [3, 8]]
    knight = board.board[0][6].piece

    hints = knight.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)


def test_move(board):
    expected_hints = [[7, 3], [7, 5],
                      [6, 2], [4, 2],
                      [3, 3], [3, 5],
                      [4, 6], [6, 6]]

    knight = board.board[4][3].piece

    hints = knight.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)
