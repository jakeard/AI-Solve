import arcade
from game import constants

class Enemy(arcade.Sprite):
    # enemy class to set enemy image and position
    def __init__(self, x, y):
        super().__init__(constants.ENEMY)
        self.center_x = x
        self.center_y = y