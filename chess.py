from chess_game._board import make_board
from chess_game.chess_game import ChessGame
from chess_game.play_game import get_user_input, game_event_loop

if __name__ == "__main__":
    game_board = make_board()
    # pawn = Pawn('x', 'y', None, None, None)
    # pawn.move()

    print('Chess')
    print(' : Rules')
    print('   : input - piece''s position x,y, second x,y = destination')
    print("   : x = row number 1 though 8")
    print("   : y = column number 1 though 8")

    player1_name = get_user_input(' : Enter player one name', is_move=False)
    player2_name = get_user_input(' : Enter player two name', is_move=False)

    print('------------------------------------------------')

    chess_game = ChessGame(game_board, player1_name, player2_name)

    game_event_loop(chess_game)
