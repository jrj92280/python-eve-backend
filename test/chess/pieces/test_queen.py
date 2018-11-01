import pytest

from chess_game.board.board import Board
from chess_game.pieces.queen import Queen
from test.utils import assert_lists_equivalent


@pytest.fixture
def board():
    board = Board()

    board.board[4][4].piece = Queen()

    """ board
    wr wh wb wk wq wb wh wr
    wp wp wp wp wp wp wp wp
    ## ## ## ## ## ## ## ##
    ## ## ## ## ## ## ## ##
    ## ## ## ## wq ## ## ##
    ## ## ## ## ## ## ## ##
    bp bp bp bp bp bp bp bp
    br bh bb bq bk bb bh br
    """
    return board


def test_blocked(board):
    expected_hints = []
    queen = board.board[0][0].piece

    hints = queen.hints(board.board)

    assert expected_hints == hints


def test_move(board):
    expected_hints = [
        # straights
        [3, 5], [4, 5], [6, 5], [7, 5],
        [5, 1], [5, 2], [5, 3], [5, 4], [5, 6], [5, 7], [5, 8],
        # diagonals
        [4, 4], [3, 3],
        [4, 6], [3, 7],
        [6, 4], [7, 3],
        [6, 6], [7, 7]
    ]
    queen = board.board[4][4].piece

    hints = queen.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)
