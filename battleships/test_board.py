from battleships.board import board


def test_board():
    b = board()
    b.add_ship(0, 0)
    b.add_ship(9, 9)

    b.display()

    assert not b.defeated()


def test_hit():
    b = board()
    b.add_ship(5, 5)

    assert b.potshot(5, 5)

    assert b.defeated()

def test_miss():
    b=board() # setting up a new board (instance)
    b.add_ship(3,3) # new ship

    assert not b.potshot(2,2) # we want this to return true i.e. pass
    assert not b.defeated() # should return true i.e. pass

