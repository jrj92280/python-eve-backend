# from chess_game.daos.player_dao import PlayerDao


def xtest_player_dao_init(mongo_database):
    player_dao = PlayerDao(mongo_database)
    assert mongo_database == player_dao._mongo_database

# def test_dao_create_and_find_player(mongo_database):
#     now = datetime.now()
#     then = datetime.now() + timedelta(days=1)
#
#     player = Player(start_date=now, end_date=then)
#     player_dao = PlayerDao(mongo_database)
#
#     player_id = player_dao.create(player)
#     loaded_player = player_dao.find_by_id(player_id)
#
#     assert loaded_player['_id']
#     assert f'{now:%Y-%m-%d %H:%M:%S}' == loaded_player['start_date']
#     assert f'{then:%Y-%m-%d %H:%M:%S}' == loaded_player['end_date']
#
#
# def test_dao_create_and_find_players(mongo_database):
#     player = Player()
#     player_dao = PlayerDao(mongo_database)
#
#     player_dao.create(player)
#     player_id = player_dao.create(player)
#     loaded_players = player_dao.find_all()
#
#     assert len(loaded_players) > 1
#     assert len([player for player in loaded_players if player_id == str(player['_id'])])
