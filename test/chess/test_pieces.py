from chess_game.pieces.bishop import Bishop
from chess_game.pieces.king import King
from chess_game.pieces.knight import Knight
from chess_game.pieces.pawn import Pawn
from chess_game.pieces.queen import Queen
from chess_game.pieces.rook import Rook


def test_piece_init():
    pawn = Pawn()
    rook = Rook(is_white=False)
    bishop = Bishop()
    knight = Knight()
    queen = Queen()
    king = King()

    assert pawn.color == 'white'
    assert rook.color == 'black'
    assert bishop.color == 'white'
    assert knight.color == 'white'
    assert queen.color == 'white'
    assert king.color == 'white'
