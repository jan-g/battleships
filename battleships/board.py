class board ():

    def __init__(self):
        self.ship = []
        self.sunk = []

    def add_ship (self,x,y):
        self.ship.append((x,y))

    def potshot(self,x,y):
        try:
            self.ship.remove((x,y))
            self.sunk.append((x,y))
            return True
        except:
            return False # this is a miss


    def defeated(self):
        return len(self.ship) == 0

    def display(self):
        print("  0123456789")
        for y in range(10):
            line = ""
            for x in range(10):
                if (x, y) in self.ship:
                    line += "S"
                elif (x, y) in self.sunk:
                    line += "X"
                else:
                    line += "."
            print(y, line)
