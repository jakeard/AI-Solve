import arcade
import random

class Input():
    def get_input(self):
        num = random.randint(1, 10)
        
        if num == 1:
            return 'jump'
        else:
            return 'right'
            