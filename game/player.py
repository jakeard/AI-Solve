import arcade
from game.input import Input

class Player(arcade.Sprite):
    # player class sets original x and y coordinates, and player image
    def __init__(self, x, y, id):
        super().__init__(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", 1)
        self.center_x = x
        self.center_y = y
        self.id = id
        self.input = Input()
        self.moves = []

    def give_input(self):
        # returns a move that the player makes
        move = self.input.get_input()
        self.add_move_list(move)
        return move
    
    def add_move_list(self, move):
        # adds the move and the player's location to the self.moves list for future retrieval
        self.moves.append((move, self.center_x))
    
    def get_move_list(self):
        # returns the self.moves list
        return self.moves
    
    def get_id(self):
        # returns the player's id
        return self.id
    
    def store_info(self):
        # returns the self.moves list and the player's x coordinate
        return self.get_move_list(), self.center_x
    
    def update(self):
        # The player's update class, runs every game tick, updates player
        super().update()