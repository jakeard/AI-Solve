import arcade
import random

class Input():
    # input class gets a random number and returns a move that is either go right or jump
    def get_input(self):
        num = random.randint(1, 10)
        
        if num == 1:
            return 'jump'
        else:
            return 'right'
            