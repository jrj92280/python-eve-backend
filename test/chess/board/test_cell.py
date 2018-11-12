from chess_game.models.cell import Cell


def test_cell_init():
    cell = Cell(1, 2, is_white=True)

    assert cell.x == 1
    assert cell.y == 2
    assert cell.color == 'white'
    assert not cell.piece
