import arcade
from game import constants
from game.player import Player
from game.walls import Walls
from game.input import Input
from game.enemy import Enemy
from game.flag import Flag
from game.collisions import Collisions
from game.win import Win
import random

class Director(arcade.View):
    # Director class controls overall game loop and functionality
    def __init__(self, base=[]):
        super().__init__()
        # needed variables to setup the game
        self.sprites = {}
        self.sprites['players'] = None
        self.sprites['walls'] = None
        self.sprites['enemies'] = None
        self.sprites['flag'] = None
        self.input = Input()
        self.collisions = Collisions()
        self.physics_engines = []
        self.dead = []
        self.moves = []
        self.base = base
    
    def setup(self):
        # sets up the game and fills the variables created in __init__
        self.camera = arcade.Camera(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

        for key in self.sprites:
            self.sprites[key] = arcade.SpriteList()
        
        for i in range(5):
            player = Player(100, 200, i)
            self.sprites['players'].append(player)

        for i in range(0, 6401, 64):
            if i not in range(500, 1150) and i not in range(4300, 4500):  
                wall = Walls(i, 94)
                self.sprites['walls'].append(wall)
        wall = Walls(600, 250)
        self.sprites['walls'].append(wall)
        wall = Walls(800, 375)
        self.sprites['walls'].append(wall)
        
        for i in range(1000, 6401, 1000):
            enemy = Enemy(i, 170)
            self.sprites['enemies'].append(enemy)

        flag = Flag(6400, 150)
        self.sprites['flag'].append(flag)

        for i in self.sprites['players']:
            self.physics_engines.append(arcade.PhysicsEnginePlatformer(i, gravity_constant=1, walls=self.sprites['walls']))
        
        if len(self.base) != 0:
            self.base.reverse()
            self.moves = self.base
        
        arcade.set_background_color(arcade.color.SKY_BLUE)
    
    def on_draw(self):
        # part of game loop, draws all sprites and camera position
        arcade.start_render()

        self.camera.use()

        for key in self.sprites:
            self.sprites[key].draw()
        self.move()
    
    def move(self):
        # if a move list exists, then it takes a move from that. Otherwise, 
        # it gets a random move for each player and executes it
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
            if len(self.moves) == 0:
                move = None
    
    def center_camera_to_player(self):
        # moves the camera to the center of the player, changes players if player[0] has died
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
        # part of game loop, controls updates
        for player in self.sprites['players']:
            # update players positions
            player.update()
        for i in self.physics_engines:
            # update physics engine for each player
            i.update()
        info = self.collisions.execute(self.sprites) # contains moves list, id of deceased sprites
        if info == True:
            # a player has reached the end of the level, show win screen
            view = Win()
            view.on_show()
            self.window.show_view(view)
        else:
            if len(info) != 0:
                # append the information from the dead players to the self.dead list
                for i in info:
                    self.dead.append(i)
            if len(self.sprites['players']) != 0:
                # recenter camera to new player[0], if it exists
                self.center_camera_to_player()
            else:
                # if all players are dead, start a new generation with the last 90 
                # moves removed, and the rest as the base for that next generation
                info = self.new_gen()
                for _ in range(90):
                    try:
                        info.pop()
                    except:
                        pass
                self.dead = []
                # restarts the game with the moves list as a base
                self.__init__(info)
                self.setup()

    def new_gen(self):
        # sorts the dead players list by shortest to farthest distance made along the x-axis
        self.dead.sort(key=lambda x:x[1])
        # returns the move list of the player that made it the farthest
        return self.dead.pop()[0]
        
        

