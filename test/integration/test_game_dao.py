import pytest

from chess_game.daos.game_dao import GameDao
from chess_game.daos.mongo import MongoDatabase
from chess_game.models.game import Game


@pytest.fixture
def mongo_database():
    mongo_database = MongoDatabase()
    return mongo_database


def test_game_dao_init(mongo_database):
    game_dao = GameDao(mongo_database)
    assert mongo_database == game_dao._mongo_database


from datetime import datetime, timedelta


def test_dao_create_and_find_game(mongo_database):
    now = datetime.now()
    then = datetime.now() + timedelta(days=1)

    game = Game(start_date=now, end_date=then)
    game_dao = GameDao(mongo_database)

    game_id = game_dao.create(game)
    loaded_game = game_dao.find_by_id(game_id)

    assert loaded_game['_id']
    assert f'{now:%Y-%m-%d %H:%M:%S%z}' == loaded_game['start_date']
    assert f'{then:%Y-%m-%d %H:%M:%S%z}' == loaded_game['end_date']


def test_dao_create_and_find_games(mongo_database):
    game = Game()
    game_dao = GameDao(mongo_database)

    game_dao.create(game)
    game_id = game_dao.create(game)
    loaded_games = game_dao.find_all()

    assert len(loaded_games) > 1
    assert len([game for game in loaded_games if game_id == str(game['_id'])])
