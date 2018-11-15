import pytest

from chess_game.models.board import Board
from chess_game.pieces.pawn import Pawn


@pytest.fixture
def board():
    board = Board()

    # single move only
    board.board[1][1].piece = None
    board.board[2][1].piece = Pawn()
    board.board[2][1].piece.has_moved = True

    # piece block and attack black and not attack white
    board.board[1][3].piece = None
    board.board[3][3].piece = Pawn()
    board.board[3][3].piece.has_moved = True

    board.board[1][2].piece = None
    board.board[4][2].piece = Pawn()
    board.board[4][2].piece.has_moved = True

    board.board[6][3].piece = None
    board.board[4][3].piece = Pawn(is_white=False)
    board.board[4][3].piece.has_moved = True

    board.board[6][4].piece = None
    board.board[4][4].piece = Pawn(is_white=False)
    board.board[4][4].piece.has_moved = True

    board.board[6][5].piece = None
    board.board[2][5].piece = Pawn(is_white=False)
    board.board[2][5].piece.has_moved = True

    board.board[6][6].piece = None
    board.board[5][6].piece = Pawn(is_white=False)
    board.board[5][6].piece.has_moved = True

    board.board[6][7].piece = None
    board.board[2][7].piece = Pawn(is_white=False)
    board.board[2][7].piece.has_moved = True

    """ board
    wr0 wh0 wb0 wk0 wq0 wb0 wh0 wr0
    wp0 ### ### ### wp0 wp0 wp0 wp0
    ### wp1 ### ### ### bp1 ### bp1
    ### ### ### wp1 ### ### ### ###
    ### ### wp1 bp1 bp1 ### ### ###
    ### ### ### ### ### ### bp1 ###
    bp0 bp0 bp0 ### ### ### ### ###
    br0 bh0 bb0 bk0 bq0 bb0 bh0 br0
    """

    return board


def test_first_move(board):
    expected_hints = [[3, 1], [4, 1]]
    pawn = board.board[1][0].piece

    hints = pawn.hints(board.board)

    assert expected_hints == hints


def test_first_move_black(board):
    expected_hints = [[6, 1], [5, 1]]
    pawn = board.board[6][0].piece

    hints = pawn.hints(board.board)

    assert expected_hints == hints


def test_move(board):
    expected_hints = [[4, 2]]
    pawn = board.board[2][1].piece

    hints = pawn.hints(board.board)

    assert expected_hints == hints


def test_move_black(board):
    expected_hints = [[5, 7]]
    pawn = board.board[5][6].piece

    hints = pawn.hints(board.board)

    assert expected_hints == hints


def test_blocked(board):
    expected_hints = []
    pawn = board.board[1][7].piece

    hints = pawn.hints(board.board)

    assert expected_hints == hints


def test_blocked_black(board):
    expected_hints = []
    pawn = board.board[4][3].piece

    hints = pawn.hints(board.board)

    assert expected_hints == hints


def test_attack(board):
    expected_hints = [[5, 5]]
    pawn = board.board[3][3].piece

    hints = pawn.hints(board.board)

    assert expected_hints == hints


def test_attack_black(board):
    expected_hints = [[2, 5], [2, 7]]
    pawn = board.board[2][5].piece

    hints = pawn.hints(board.board)

    assert expected_hints == hints
