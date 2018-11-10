import pytest

from chess_game.board.board import Board
from chess_game.pieces.bishop import Bishop
from test.utils import assert_lists_equivalent


@pytest.fixture
def board():
    board = Board()

    board.board[0][5].piece = None
    board.board[4][4].piece = Bishop()
    board.board[4][4].piece.has_moved = True

    """ board
    wr0 wh0 wb0 wk0 wq0 ### wh0 wr0
    wp0 wp0 wp0 wp0 wp0 wp0 wp0 wp0
    ### ### ### ### ### ### ### ###
    ### ### ### ### ### ### ### ###
    ### ### ### ### wb1 ### ### ###
    ### ### ### ### ### ### ### ###
    bp0 bp0 bp0 bp0 bp0 bp0 bp0 bp0
    br0 bh0 bb0 bk0 bq0 bb0 bh0 br0
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
