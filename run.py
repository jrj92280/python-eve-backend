import os
from datetime import datetime

from eve import Eve
from flask import render_template, request, jsonify

from chess_game.daos.board_dao import BoardDao
from chess_game.daos.game_dao import GameDao
from chess_game.daos.mongo import MongoDatabase
from chess_game.daos.player_dao import PlayerDao
from chess_game.models.board import Board
from chess_game.models.game import Game
# Heroku support: bind to PORT if defined, otherwise default to 5000.
from chess_game.models.player import Player

if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

os.environ['FLASK_ENV'] = 'development'

app = Eve(template_folder=tmpl_dir,
          static_folder=static_dir)

board_dao = BoardDao(MongoDatabase())
game_dao = GameDao(MongoDatabase())
player_dao = PlayerDao(MongoDatabase())


@app.route('/hello')
def hello():
    return "Hello Jason!"


# games
@app.route('/chess/game')
def chess_game():
    game = Game()
    return render_template('game.html', game=game)


@app.route('/chess/games')
def games():
    boards = board_dao.find_all()
    _games = game_dao.find_all()
    return render_template('games.html', games=_games, boards=boards)


@app.route('/chess/game', methods=['POST'])
def create_game():
    # form values
    player_one_value = get_arg("playerOneId")
    player_one_id = player_one_value.split(":")[0]
    player_one = None  # load player with player_dao

    player_two_value = get_arg("playerTwoId")
    player_two_id = player_two_value.split(":")[0]
    player_two = None  # load player with player_dao

    name = get_arg("name")

    # default values
    board = Board()
    board_id = board_dao.create(board)
    board = board_dao.find_by_id(board_id)

    start_date = datetime.now()
    game_data = {'move_count': 0, 'player_one_move_count': 0, 'player_two_move_count': 0, 'turn': 'player_one'}
    status = "New"

    game = Game(player_one=player_one, player_two=player_two, board=board, game_data=game_data, start_date=start_date,
                status=status, name=name)
    game_id = game_dao.create(game)

    _games = game_dao.find_all()
    return render_template('games.html', game_id=game_id, games=_games)


# players
@app.route('/chess/player')
def chess_player():
    player = Player()
    return render_template('player.html', player=player)


@app.route('/chess/players')
def players():
    boards = board_dao.find_all()
    _players = player_dao.find_all()
    return render_template('players.html', players=_players, boards=boards)


@app.route('/chess/player', methods=['POST'])
def create_player():
    # form values
    name = get_arg("name")
    start_date = datetime.now()

    player = Player(start_date=start_date, name=name)
    player_id = player_dao.create(player)

    _players = player_dao.find_all()
    return render_template('players.html', player_id=player_id, players=_players)


# profile
@app.route('/chess/profile', methods=["GET"])
def chess_profile():
    player = Player(name="Jason Jacobs", stats={'games': 100, 'wins': 97, 'losses': 3, 'time': 6000}, games=[],
                    start_date=datetime.now(), _id="mongo_id")

    return render_template('profile.html', player=player)


# profile
@app.route('/chess/profile', methods=["POST"])
def chess_profile_update():
    # TODO save player profile
    player = Player(name="Jason Jacobs", stats={'games': 100, 'wins': 97, 'losses': 3, 'time': 6000}, games=[],
                    start_date=datetime.now(), _id="mongo_id")

    return render_template('profile.html', player=player)


# login
@app.route('/chess/logine', methods=["GET"])
def chess_login():
    player = Player(name="Jason Jacobs", stats={'games': 100, 'wins': 97, 'losses': 3, 'time': 6000}, games=[],
                    start_date=datetime.now(), _id="mongo_id")

    return render_template('login.html', player=player)


# login
@app.route('/chess/login', methods=["POST"])
def chess_login_user():
    # TODO save player profile
    player = Player(name="Jason Jacobs", stats={'games': 100, 'wins': 97, 'losses': 3, 'time': 6000}, games=[],
                    start_date=datetime.now(), _id="mongo_id")

    return render_template('login.html', player=player)



# play game
@app.route('/chess')
def chess():
    board = Board()
    board_id = board_dao.create(board)
    player_one = get_arg('user')

    # pass board id into variable
    return render_template('chess.html', board=board, player_one=player_one, board_id=board_id)


@app.route('/chess/hints', methods=['POST'])
def chess_hint():
    # receive board id from args
    board_id = get_arg('board_id')
    row = get_arg('row')
    column = get_arg('column')

    board = board_dao.find_by_id(board_id)
    piece = board.board[int(row) - 1][int(column) - 1].piece
    hints = piece.hints(board.board)

    return jsonify(hints)


@app.route('/chess/move', methods=['POST'])
def chess_move():
    board_id = get_arg('board_id')
    selected = get_arg('selected[]', is_list=True)
    targeted = get_arg('targeted[]', is_list=True)

    board = board_dao.find_by_id(board_id)
    game_board = board.board

    piece = game_board[int(selected[0]) - 1][int(selected[1]) - 1].piece
    game_board[int(selected[0]) - 1][int(selected[1]) - 1].piece = None

    game_board[int(targeted[0]) - 1][int(targeted[1]) - 1].piece = piece
    piece.has_moved = True

    board_dao.update(board_id, board)
    print(board)
    return jsonify({'targeted': targeted, 'selected': selected})


def get_arg(name, *, is_list=False):
    if is_list:
        return request.form.getlist(name)

    return request.args.get(name) or request.form.get(name)


if __name__ == '__main__':
    app.run(host=host, port=port)
