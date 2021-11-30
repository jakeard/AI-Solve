import arcade
from game import constants

class Walls(arcade.Sprite):
    def __init__(self, x, y):
        img = constants.WALL
        super().__init__(img)
        self.center_x = x
        self.center_y = y
        