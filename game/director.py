import arcade
from game import constants
from game.player import Player
from game.walls import Walls
from game.input import Input
from game.enemy import Enemy
from game.collisions import Collisions
import random

class Director(arcade.View):
    def __init__(self, base=[]):
        super().__init__()
        self.sprites = {}
        self.sprites['players'] = None
        self.sprites['walls'] = None
        self.input = Input()
        self.collisions = Collisions()
        self.physics_engines = []
        self.sprites['enemies'] = None
        self.dead = []
        self.moves = []
        self.base = base
    
    def setup(self):
        self.camera = arcade.Camera(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

        for key in self.sprites:
            self.sprites[key] = arcade.SpriteList()
        
        for i in range(5):
            player = Player(100, 200, i)
            self.sprites['players'].append(player)

        for i in range(0, 6401, 64):
            if i not in range(500, 1100):  
                wall = Walls(i, 94)
                self.sprites['walls'].append(wall)
        wall = Walls(600, 250)
        self.sprites['walls'].append(wall)
        
        for i in range(600, 6401, 1000):
            enemy = Enemy(i, 170)
            self.sprites['enemies'].append(enemy)

        for i in self.sprites['players']:
            # self.physics_engine = arcade.PhysicsEnginePlatformer(i, gravity_constant=1, walls=self.sprites['walls'])
            self.physics_engines.append(arcade.PhysicsEnginePlatformer(i, gravity_constant=1, walls=self.sprites['walls']))
        
        if len(self.base) != 0:
            self.base.reverse()
            self.moves = self.base
        
        arcade.set_background_color(arcade.color.SKY_BLUE)
    
    def on_draw(self):
        arcade.start_render()

        self.camera.use()

        for key in self.sprites:
            self.sprites[key].draw()
        self.move()
    
    def move(self):
        move = None
        location = None
        if len(self.moves) != 0:
            info = self.moves.pop()
            move = info[0]
            location = info[1]
        for player in self.sprites['players']:
            if move is None:
                move = player.give_input()
            else:
                player.add_move_list(move)
            id = player.get_id()
            if location is not None:
                if player.center_x != location:
                    player.center_x = location
            if move == 'right':
                player.change_x = 5
            elif move == 'jump':
                if self.physics_engines[id].can_jump():
                    player.change_y = 13
                    num = random.randint(1, 2)
                    if num == 1:
                        player.change_x = 5
                    elif num == 2:
                        num = random.randint(1, 3)
                        if num != 1:
                            player.change_x = -5
            elif move == 'left':
                player.change_x = -5
    
    # def find_move(self, move, id, player):
    #     if move == 'right':
    #         player.change_x = 5
    #     elif move == 'jump':
    #         if self.physics_engines[id].can_jump():
    #             player.change_y = 13
    #         num = random.randint(1, 2)
    #         if num == 1:
    #             player.change_x = 5
    #         elif num == 2:
    #             num = random.randint(1, 3)
    #             if num != 1:
    #                 player.change_x = -5
    #     elif move == 'left':
    #         player.change_x = -5
    
    def center_camera_to_player(self):
        try:
            screen_center_x = self.sprites['players'][0].center_x - (self.camera.viewport_width / 2)
            screen_center_y = self.sprites['players'][0].center_y - (self.camera.viewport_height / 2)
        except:
            screen_center_x = self.sprites['enemies'][0].center_x - (self.camera.viewport_width / 2)
            screen_center_y = self.sprites['enemies'][0].center_y - (self.camera.viewport_height / 2)

        # Don't let camera travel past 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def on_update(self, delta_time):
        for player in self.sprites['players']:
            player.update()
        for i in self.physics_engines:
            i.update()
        info = self.collisions.execute(self.sprites)
        if len(info) != 0:
            for i in info:
                self.dead.append(i)
        if len(self.sprites['players']) != 0:
            self.center_camera_to_player()
        else:
            info = self.new_gen()
            for _ in range(90):
                try:
                    info.pop()
                except:
                    pass
            self.dead = []
            self.__init__(info)
            self.setup()

    def new_gen(self):
        # max = -100
        self.dead.sort(key=lambda x:x[1])
        # for i in self.dead:
        #     if i[1] > max:
        #         max = i[1]
        return self.dead.pop()[0]
        # self.setup(self.dead[0])
        

