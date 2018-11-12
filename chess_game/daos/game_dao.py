from bson import ObjectId


class GameDao:
    def __init__(self, mongo_database):
        self._mongo_database = mongo_database
        self._collection = 'games'

    def create(self, game):
        game_json = game.to_json()
        game_id = self._mongo_database.create(self._collection, game_json)
        return game_id

    def find_all(self):
        results = [result for result in self._mongo_database.find(self._collection, None)]
        return results

    def find_by_id(self, game_id):
        game_model = self._mongo_database.get(self._collection, game_id)
        return game_model

    def update(self, game_id, game):
        return self._mongo_database.mongo_db[self._collection].update_one(
            {'_id': ObjectId(game_id)}, {"$set": game})
