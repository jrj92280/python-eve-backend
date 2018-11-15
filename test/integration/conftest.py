import pytest

from chess_game.daos.mongo import MongoDatabase


@pytest.fixture(scope="session")
def mongo_database():
    mongo_database = MongoDatabase()
    return mongo_database
