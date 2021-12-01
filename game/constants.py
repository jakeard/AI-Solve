import os

SCREEN_WIDTH = 1216
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Solve Level"

CHARACTER_SCALING = .9
SPRITE_SCALING = 1

PATH = os.path.dirname(os.path.abspath(__file__))

# Asset Pathing
WALL = os.path.join(PATH, '..', 'images', 'wall.png')
ENEMY = os.path.join(PATH, '..', 'images', 'ghost.png')
FLAG = os.path.join(PATH, '..', 'images', 'flag.png')
WIN_SCREEN = os.path.join(PATH, '..', 'images', 'win.png')