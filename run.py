import os

from eve import Eve
from flask import render_template, request

# Heroku support: bind to PORT if defined, otherwise default to 5000.
from chess_game._board import make_board

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


@app.route('/chess')
def chess():
    game_board = request.args.get("game_board") or request.form.get('game_board') or make_board()
    player_one = request.args.get("user") or request.form.get('user')

    board = "<br />".join(" ".join(row) for row in game_board)
    return render_template('chess.html', board=board, game_board=game_board, player_one=player_one)


if __name__ == '__main__':
    app.run(host=host, port=port)
