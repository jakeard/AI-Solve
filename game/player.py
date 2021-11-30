import arcade
from game.input import Input

class Player(arcade.Sprite):
    def __init__(self, x, y, id, moves=[]):
        super().__init__(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", 1)
        self.center_x = x
        self.center_y = y
        self.id = id
        self.input = Input()
        self.moves = moves

    def give_input(self):
        move = self.input.get_input()
        self._add_move_list(move)
        return move
    
    def _add_move_list(self, move):
        self.moves.append(move)
    
    def get_move_list(self):
        return self.moves
    
    def get_id(self):
        return self.id
    
    def store_info(self):
        return self.get_move_list(), self.center_x
    
    def update(self):
        """The player's update class. Is run every game tick."""
        super().update()