import sys
from battleships.board import Board, parse_ship_location, parse_bomb_location


ships = [("Carrier", 5),
         ("Battleship", 4),
         ("Cruiser", 3),
         ("Submarine",2),
         ("Destroyer", 2)]


def get_ships(name, guess_method):
    print("{} pick your ships!".format(name))
    print("Use: R C D for input (R: row; C: column; D = A for across, D for down)")
    player = Board()
    for ship, size in ships:
        while True:
            print()
            player.display()
            location = input("enter position of {}: ".format(ship))
            # We want three characters: the y-coord, the x-coord and an A or a D.
            try:
                x, y, dx, dy = parse_ship_location(location)
            except:
                print("Use: R C D for input (R: row; C: column; D = A for across, D for down)")
                continue

            # Try to place the ship
            try:
                player.add_ship(x, y, dx, dy, size)
            except:
                print("That ship can't go there!")
                continue

            break

    player.name = name
    player.guess = guess_method
    return player


def get_human_move():
    while True:
        try:
            x, y = parse_bomb_location(input("your guess?"))
            return x, y
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            pass


def main():
    player1 = get_ships("Player 1", get_human_move)
    player2 = get_ships("Player 2", get_human_move)

    player, other = (player2, player1)
    while not other.defeated():
        player, other = other, player

        print("{}. your turn".format(player.name))
        print()
        print("Your board:")
        player.display()

        print()
        print("Their board:")
        other.display_other()

        x, y = player.guess()

        result = other.potshot(x, y)
        if result == Board.MISS:
            print("Splash!")
        elif result == Board.NEAR:
            print("KERSPLOOSH!!")
        else:
            print("BOOM!!!")

    print("The winner is {}".format(player.name))


if __name__ == "__main__":
    main()