import os

from eve import Eve
from flask import render_template, request, jsonify

# Heroku support: bind to PORT if defined, otherwise default to 5000.
from chess_game._board import make_board
from chess_game.board.board import Board

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

os.environ['FLASK_ENV']='development'

app = Eve(template_folder=tmpl_dir,
          static_folder=static_dir)

@app.route('/hello')
def hello():
    return "Hello Jason!"


@app.route('/xchess')
def chess():
    board = Board()
    # save board

    player_one = request.args.get("user") or request.form.get('user')

    # pass board id into variable
    return render_template('chess_backend.html', board=board, player_one=player_one)


@app.route('/chess/hint', methods=['POST'])
def chess_hint():
    # receive board id from args
    game_board = request.args.get("game_board") or request.form.get('game_board')
    row = request.args.get("row") or request.form.get('row')
    column = request.args.get("column") or request.form.get('column')
    piece = game_board[row, column].piece
    hints = piece.hints()

    return jsonify(hints)


@app.route('/chess')
def chess_frontend():
    game_board = request.args.get("game_board") or request.form.get('game_board') or make_board()
    player_one = request.args.get("user") or request.form.get('user')

    board = "<br />".join(" ".join(row) for row in game_board)
    return render_template('chess.html', board=board, game_board=game_board, player_one=player_one)


if __name__ == '__main__':
    app.run(host=host, port=port)
