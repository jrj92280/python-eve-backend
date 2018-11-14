class Game:
    def __init__(self, *, player_one=None, player_two=None, board=None, game_data=None, start_date=None, end_date=None,
                 status=None, name=None, _id=None):
        self.player_one = player_one
        self.player_two = player_two
        self.board = board
        self.game_data = game_data
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.name = name
        self._id = _id

    def to_json(self):
        game_json = dict()
        game_json['player_one'] = self.player_one._id if self.player_one else None
        game_json['player_two'] = self.player_two._id if self.player_two else None
        game_json['board'] = self.board._id if self.board else None
        game_json['game_data'] = self.game_data

        start_date = f'{self.start_date:%Y-%m-%d %H:%M:%S}' if self.start_date else None
        game_json['start_date'] = start_date

        end_date = f'{self.end_date:%Y-%m-%d %H:%M:%S}' if self.end_date else None
        game_json['end_date'] = end_date

        game_json['status'] = self.status
        game_json['name'] = self.name

        if self._id:
            game_json['_id'] = self._id

        return game_json
