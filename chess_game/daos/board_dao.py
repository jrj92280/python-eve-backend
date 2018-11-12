from bson import ObjectId

from chess_game.models.board import Board


class BoardDao:
    def __init__(self, mongo_database):
        self._mongo_database = mongo_database
        self._collection = 'boards'

    def create(self, board):
        board_str = str(board)
        board_model = {"board": board_str}
        board_id = self._mongo_database.create(self._collection, board_model)
        return board_id

    def find_all(self):
        results = [result for result in self._mongo_database.find(self._collection, None)]
        return results

    def find_by_id(self, board_id):
        board_model = self._mongo_database.get(self._collection, board_id)
        board = Board.build_board(board_model['board'])
        return board

    def update(self, board_id, board):
        return self._mongo_database.mongo_db[self._collection].update_one(
            {'_id': ObjectId(board_id)}, {"$set": {'board': str(board)}})
