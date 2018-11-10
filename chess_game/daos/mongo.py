from bson import ObjectId
from pymongo import MongoClient

from chess_game.daos.environment import env


class MongoDatabase:
    def __init__(self):
        mongo_url = env("mongo_url") or "mongodb://localhost:27017/chess"
        client = MongoClient(mongo_url)
        mongo_db = client.chess

        self.mongo_db = mongo_db

    def create(self, collection: str, entity: dict) -> str:
        insert_object = self.mongo_db[collection].insert_one(entity)
        return str(insert_object.inserted_id)

    def get(self, collection: str, id: str):
        return self.mongo_db[collection].find_one({'_id': ObjectId(id)})

    def find(self, collection: str, filter: dict) -> list:
        return self.mongo_db[collection].find(filter)
