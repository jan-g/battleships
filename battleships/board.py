import numpy as np


class board ():

    def __init__(self):
        self.grid = np.zeros((10,10),dtype=int)
        self.ship = []

    def add_ship (self,x,y):
        self.ship.append((x,y))

    def potshot(self,x,y):
        pass

    def defeated(self):
        return False


