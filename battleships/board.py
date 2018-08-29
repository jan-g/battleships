class board ():

    def __init__(self):
        self.ship = []

    def add_ship (self,x,y):
        self.ship.append((x,y))

    def potshot(self,x,y):
        pass

    def defeated(self):
        return len(self.ship) == 0

    def display(self):
        print("  0123456789")
        for y in range(10):
            line = ""
            for x in range(10):
                if (x, y) in self.ship:
                    line += "S"
                else:
                    line += "."
            print(y, line)
