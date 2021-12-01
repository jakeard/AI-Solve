import arcade
from game import constants

class Flag(arcade.Sprite):
    # flag class to set flag image and position
    def __init__(self, x, y):
        super().__init__(constants.FLAG)
        self.center_x = x
        self.center_y = y
