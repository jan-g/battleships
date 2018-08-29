from battleships.board import board


ships = [["Carrier"],
		["Battleship"],
		["Cruiser"],
		["Submarine"],
		["Destroyer"]]

def main():
    player1 = get_ships("player1")
    player2 = get_ships("player1")



def get_ships(name):
    print("{}".format(name))
    player = board()
    for ship in ships:
        locationx = input("enter x position of {}".format(ship))
        locationy = input("enter y position of {}".format(ship))
        # get x and y from here
        x = int(locationx)
        y = int(locationy)
        player.add_ship(x, y)
        return player