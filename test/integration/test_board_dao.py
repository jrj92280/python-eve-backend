import pytest

from chess_game.board.board import Board
from chess_game.daos.board_dao import BoardDao
from chess_game.daos.mongo import MongoDatabase
from test.chess.pieces.test_pawn import board


@pytest.fixture
def mongo_database():
    mongo_database = MongoDatabase()
    return mongo_database


def test_board_dao_init(mongo_database):
    board_dao = BoardDao(mongo_database)
    assert mongo_database == board_dao._mongo_database


def test_dao_create_and_find_board(mongo_database):
    board = Board()
    board_dao = BoardDao(mongo_database)

    board_id = board_dao.create(board)
    loaded_board = board_dao.find_by_id(board_id)

    assert 8 == len(loaded_board.board)
    assert 8 == len(loaded_board.board[0])

    for row_index, row in enumerate(loaded_board.board):
        for cell_index, cell in enumerate(row):
            assert str(board.board[row_index][cell_index]) == str(cell)


def test_find_updated_board(mongo_database):
    updated_board = board()
    board_dao = BoardDao(mongo_database)

    board_id = board_dao.create(updated_board)
    loaded_board = board_dao.find_by_id(board_id)

    for row_index, row in enumerate(loaded_board.board):
        for cell_index, cell in enumerate(row):
            assert str(updated_board.board[row_index][cell_index]) == str(cell)
