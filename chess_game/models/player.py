class Player:
    def __init__(self, *, name=None, stats=None, games=None, start_date=None, _id=None):
        self.name = name
        self.stats = stats
        self.games = games
        self.start_date = start_date
        self._id = _id

    def to_json(self):
        game_json = dict()
        game_json['name'] = self.name
        game_json['stats'] = self.stats
        game_json['games'] = [game._id for game in self.games] if self.games else None

        start_date = f'{self.start_date:%Y-%m-%d %H:%M:%S}' if self.start_date else None
        game_json['start_date'] = start_date

        if self._id:
            game_json['_id'] = self._id

        return game_json
