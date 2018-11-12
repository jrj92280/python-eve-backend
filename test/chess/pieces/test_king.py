import pytest

from chess_game.models.board import Board
from chess_game.pieces.king import King
from chess_game.pieces.pawn import Pawn
from test.utils import assert_lists_equivalent


@pytest.fixture
def board():
    board = Board()

    board.board[4][4].piece = King()
    board.board[4][5].piece = Pawn(is_white=False)

    board.board[6][5].piece = None
    board.board[7][1].piece = None
    board.board[7][2].piece = None
    board.board[7][3].piece = None
    board.board[7][5].piece = None
    board.board[7][6].piece = None

    """ board
    wr0 wh0 wb0 wk0 wq0 wb0 wh0 wr0
    wp0 wp0 wp0 wp0 wp0 wp0 wp0 wp0
    ### ### ### ### ### ### ### ###
    ### ### ### ### ### ### ### ###
    ### ### ### ### wk0 bp0 ### ###
    ### ### ### ### ### ### ### ###
    bp0 bp0 bp0 bp0 bp0 ### bp0 bp0
    br0 ### ### ### bq0 ### ### br0
    """

    return board


def test_blocked(board):
    expected_hints = []
    king = board.board[0][0].piece

    hints = king.hints(board.board)

    assert expected_hints == hints


def test_move():
    board = Board()

    board.board[3][3].piece = King()

    """ board
    wr0 wh0 wb0 wk0 wq0 wb0 wh0 wr0
    wp0 wp0 wp0 wp0 wp0 wp0 wp0 wp0
    ### ### ### ### ### ### ### ###
    ### ### ### wk0 ### ### ### ###
    ### ### ### ### ### ### ### ###
    ### ### ### ### ### ### ### ###
    bp0 bp0 bp0 bp0 bp0 bp0 bp0 bp0
    br0 bh0 bb0 bk0 bq0 bb0 bh0 br0
    """

    expected_hints = [
        [3, 3], [3, 4], [3, 5], [4, 3], [4, 5], [5, 3], [5, 4], [5, 5]
    ]
    king = board.board[3][3].piece

    hints = king.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)


def test_move_with_threat(board):
    expected_hints = [
        [4, 4], [4, 6], [5, 6], [5, 4]
    ]
    king = board.board[4][4].piece

    hints = king.hints(board.board)

    assert_lists_equivalent(expected_hints, hints)
