import arcade
from game import constants

class Walls(arcade.Sprite):
    # walls class to set walls image and position
    def __init__(self, x, y):
        super().__init__(constants.WALL)
        self.center_x = x
        self.center_y = y
        