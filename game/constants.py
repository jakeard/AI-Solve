import os

SCREEN_WIDTH = 1216
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Solve Level"

CHARACTER_SCALING = .9
SPRITE_SCALING = 1

PATH = os.path.dirname(os.path.abspath(__file__))

# Asset Pathing
PLAYER = os.path.join(PATH, '..', 'assets','kenney_assets', 'Characters', 'character_000')
WALL = os.path.join(PATH, '..', 'images', 'tile_0006.png')
ENEMY = os.path.join(PATH, '..', 'images', 'ghost.png')