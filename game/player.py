import arcade
from game.input import Input

class Player(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", 1)
        self.center_x = x
        self.center_y = y
        self.input = Input()
        self.moves = []

    def give_input(self):
        move = self.input.get_input()
        self._add_move_list(move)
        return move
    
    def _add_move_list(self, move):
        self.moves.append(move)
    
    def get_move_list(self):
        return self.moves
    
    def update(self):
        """The player's update class. Is run every game tick."""
        super().update()