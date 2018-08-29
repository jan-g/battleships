from battleships.board import board


def test_board():
    b = board()
    b.add_ship(0, 0)
    b.add_ship(9, 9)

    b.display()

    assert False
