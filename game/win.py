import arcade
from game import constants

class Win(arcade.View):
    # win class to set the view to the win screen when a player has won
    def __init__(self):
        super().__init__()
    
    def on_show(self):
        arcade.set_viewport(0, constants.SCREEN_WIDTH, 0, constants.SCREEN_HEIGHT)
        self.texture = arcade.load_texture(constants.WIN_SCREEN)
    
    def on_draw(self):
        arcade.start_render
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)