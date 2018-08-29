from board import board


ships = ["Carrier",
		"Battleship",
		"Cruiser",
		"Submarine",
		"Destroyer"]


def get_ships(name):
    print("{} pick your ships!".format(name))
    player = board()
    for ship in ships:
        locationx = input("enter x position of {}: ".format(ship))
        locationy = input("enter y position of {}: ".format(ship))
        # get x and y from here
        x = int(locationx)
        y = int(locationy)
        player.add_ship(x, y)

    return player


def main():
    player1 = get_ships("Player 1")
    player2 = get_ships("Player 2")
    print(player1)
    print(player2)

if __name__ == "__main__":
	main()