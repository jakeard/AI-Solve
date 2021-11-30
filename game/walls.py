import arcade

class Walls(arcade.Sprite):
    def __init__(self, x, y):
        img = 'images/tile_0006.png'
        super().__init__(img)
        self.center_x = x
        self.center_y = y
        