"""   Eve Demo
    ~~~~~~~~
    A demostration of a simple API powered by Eve REST API.
    The live demo is available at eve-demo.herokuapp.com. Please keep in mind
    that the it is running on Heroku's free tier using a free MongoHQ
    sandbox, which means that the first request to the service will probably
    be slow. The database gets a reset every now and then.
    :copyright: (c) 2016 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os

from flask import render_template
from eve import Eve

# Heroku support: bind to PORT if defined, otherwise default to 5000.
from chess_game.board import make_board
from chess_game.chess_game import ChessGame

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

app = Eve(template_folder=tmpl_dir,
          static_folder=static_dir)


@app.route('/hello')
def hello():
    return "Hello Jason!"


@app.route('/chess')
def chess():
    game_board = make_board()
    board = "<br />".join(" ".join(row) for row in game_board)
    return render_template('chess.html', board=board)


if __name__ == '__main__':
    app.run(host=host, port=port)
