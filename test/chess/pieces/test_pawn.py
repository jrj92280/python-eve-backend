import pytest

from chess_game.board.board import Board
from chess_game.pieces.pawn import Pawn


@pytest.fixture
def board():
    board = Board()

    # single move only
    board.board[1][1].piece = None
    board.board[2][1].piece = Pawn()

    # piece block and attack black and not attack white
    board.board[1][3].piece = None
    board.board[3][3].piece = Pawn()

    board.board[1][2].piece = None
    board.board[4][2].piece = Pawn()

    board.board[6][3].piece = None
    board.board[4][3].piece = Pawn(is_white=False)

    board.board[6][4].piece = None
    board.board[4][4].piece = Pawn(is_white=False)

    board.board[6][7].piece = None
    board.board[2][7].piece = Pawn(is_white=False)

    """ board
    wr wh wb wk wq wb wh wr
    wp ## ## ## wp wp wp wp
    ## wp ## ## ## ## ## bp
    ## ## ## wp ## ## ## ##
    ## ## wp bp bp ## ## ##
    ## ## ## ## ## ## ## ##
    bp bp bp ## ## bp bp ##
    br bh bb bq bk bb bh br
    """
    return board


def test_first_move(board):
    expected_hints = [[3, 1], [4, 1]]
    first_move_pawn = board.board[1][0].piece

    hints = first_move_pawn.hints(board.board)

    assert expected_hints == hints


def test_not_first_move(board):
    expected_hints = [[4, 2]]
    first_move_pawn = board.board[2][1].piece

    hints = first_move_pawn.hints(board.board)

    assert expected_hints == hints


def test_blocked(board):
    expected_hints = []
    first_move_pawn = board.board[1][7].piece

    hints = first_move_pawn.hints(board.board)

    assert expected_hints == hints


def test_attack(board):
    expected_hints = [[5, 5]]
    first_move_pawn = board.board[3][3].piece

    hints = first_move_pawn.hints(board.board)

    assert expected_hints == hints
