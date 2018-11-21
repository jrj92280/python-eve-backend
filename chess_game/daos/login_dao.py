from bson import ObjectId


class LoginDao:
    def __init__(self, mongo_database, firebase):
        self._mongo_database = mongo_database
        self._collection = 'players'

    def create(self, player):
        player_json = player.to_json()
        player_id = self._mongo_database.create(self._collection, player_json)
        return player_id

    def find_all(self):
        results = [result for result in self._mongo_database.find(self._collection, None)]
        return results

    def find_by_id(self, player_id):
        player_model = self._mongo_database.get(self._collection, player_id)
        return player_model

    def update(self, player_id, player):
        return self._mongo_database.mongo_db[self._collection].update_one(
            {'_id': ObjectId(player_id)}, {"$set": player})
