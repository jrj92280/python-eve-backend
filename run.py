import os

from eve import Eve
from flask import render_template, request, jsonify

# Heroku support: bind to PORT if defined, otherwise default to 5000.
from chess_game._board import make_board
from chess_game.board.board import Board
from chess_game.daos.board_dao import BoardDao
from chess_game.daos.mongo import MongoDatabase

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


@app.route('/hello')
def hello():
    return "Hello Jason!"


@app.route('/xchess')
def chess():
    board = Board()
    board_id = board_dao.create(board)
    player_one = get_arg('user')

    # pass board id into variable
    return render_template('chess_backend.html', board=board, player_one=player_one, board_id=board_id)


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

    print()


@app.route('/chess')
def chess_frontend():
    game_board = get_arg('game_board') or make_board()
    player_one = get_arg('user')

    board = "<br />".join(" ".join(row) for row in game_board)
    return render_template('chess.html', board=board, game_board=game_board, player_one=player_one)


def get_arg(name, *, is_list=False):
    if is_list:
        return request.form.getlist(name)

    return request.args.get(name) or request.form.get(name)


if __name__ == '__main__':
    app.run(host=host, port=port)
