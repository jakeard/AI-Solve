import arcade
import random

class Input():
    def get_input(self):
        num = random.randint(1, 2)
        
        if num == 1:
            return 'right'
        elif num == 2:
            num = random.randint(1, 3)
            if num == 1:
                return 'left'
            else:
                return 'right'
            