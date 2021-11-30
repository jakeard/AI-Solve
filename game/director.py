import arcade
from game import constants
from game.player import Player
from game.walls import Walls
from game.input import Input
import time

class Director(arcade.View):
    def __init__(self):
        super().__init__()
        self.sprites = {}
        self.sprites['players'] = None
        self.sprites['walls'] = None
        self.input = Input()
        # self.sprites['enemies'] = None
    
    def setup(self):
        self.camera = arcade.Camera(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

        for key in self.sprites:
            self.sprites[key] = arcade.SpriteList()
        
        for _ in range(5):
            player = Player(100, 200)
            self.sprites['players'].append(player)

        for i in range(0, 6401, 64):
            wall = Walls(i, 94)
            self.sprites['walls'].append(wall)
        
        arcade.set_background_color(arcade.color.KHAKI)
    
    def on_draw(self):
        arcade.start_render()

        self.camera.use()

        for key in self.sprites:
            self.sprites[key].draw()
        self.move()
    
    def move(self):
        for player in self.sprites['players']:
            move = player.give_input()
            if move == 'right':
                player.change_x = 5
            elif move == 'left':
                player.change_x = -5
        # self.wait()
    
    def center_camera_to_player(self):
        screen_center_x = self.sprites['players'][0].center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.sprites['players'][0].center_y - (self.camera.viewport_height / 2)

        # Don't let camera travel past 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def on_update(self, delta_time):
        # start_time = time.time()
        # for player in self.sprites['players']:
        #     player.change_x = 0
        for player in self.sprites['players']:
            player.update()
        self.center_camera_to_player()
