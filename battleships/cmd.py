from battleships.board import board


"""ships = ["Carrier",
		"Battleship",
		"Cruiser",
		"Submarine",
		"Destroyer"]"""

ships = ["Carrier"]


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

    player1_turn = True
    winner = False
    while winner == False:
        if player1_turn:
            print("Player 1, your go")
            current_player = player1
            player_name = "Player 1"
            other_player = player2
        else:
            print("Player 2, your go")
            current_player = player2
            player_name = "Player 2"
            other_player = player1

        x = int(input("Enter x"))
        y = int(input("Enter y"))

        other_player.potshot(x,y)

        if other_player.defeated():
            winner = True
            other_player.display()
            print("The winner is {}".format(player_name))

        player1_turn = not player1_turn
		

if __name__ == "__main__":
	main()