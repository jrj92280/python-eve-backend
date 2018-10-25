from chess_game.board.cell import Cell


def test_cell_init():
    cell = Cell(1, 2, 'white', None)

    assert cell.x == 1
    assert cell.y == 2
    assert cell.color == 'white'
    assert cell.piece == None
