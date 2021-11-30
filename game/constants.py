import os

SCREEN_WIDTH = 1216 # Was originally 800
SCREEN_HEIGHT = 768 # Was originally 600
SCREEN_TITLE = "Move with a Sprite Animation Example"

WIDTH_RATIO = SCREEN_WIDTH / 800
HEIGHT_RATIO = SCREEN_HEIGHT / 600


# CHARACTER_SCALING = 2.2

# COIN_SCALE = 0.5
# COIN_COUNT = 50
CHARACTER_SCALING = .9
SPRITE_SCALING = 1

# How fast to move, and how fast to run the animation
# MOVEMENT SPEED MUST BE A POWER OF 2
MOVEMENT_SPEED = 4
UPDATES_PER_FRAME = 1

# Constants used to track if the player is facing left or right
RIGHT_FACING = 1
LEFT_FACING = 0

# One tile is how many pixels?
TILE_SIZE = 64

PATH = os.path.dirname(os.path.abspath(__file__))

# Asset Pathing
NEW_PLAYER_SPRITE = os.path.join(PATH, '..', 'assets', 'images', 'character_000') # Trim off the last digit and .png 
PLAYER_SPRITE = os.path.join(PATH, '..', 'assets','kenney_assets', 'Characters', 'character_000') # Trim off the last digit and .png 
WALL_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Tiles', 'tile_0006.png')
BACKGROUND_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Tiles', 'tile_0122.png')
MOVING_WALL_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Tiles', 'tile_0026.png')
FLAG_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Tiles', 'tile_0112.png')
DOOR_SPRITE = os.path.join(PATH, '..', 'assets', 'images', 'tile_0150.png')
GRASS_SPRITE = os.path.join(PATH, '..', 'assets', 'images', 'grass5.png')
KEY_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Tiles', 'tile_0027.png')
LOCK_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Tiles', 'tile_0028.png')
BUTTON_SPRITE = os.path.join(PATH, '..', 'assets', 'images', 'button.png')
BUTTON_PRESSED_SPRITE = os.path.join(PATH, '..', 'assets', 'images', 'button_pressed.png')
BACKGROUND_SPRITE = os.path.join(PATH, '..', 'assets', 'kenney_assets', 'Background', 'background_0002.png')
START_SCREEN = os.path.join(PATH, '..', 'assets', 'images', 'start_screen.png')
WIN_SCREEN = os.path.join(PATH, '..', 'assets', 'images', 'win.png')
LOSE_SCREEN = os.path.join(PATH, '..', 'assets', 'images', 'you_lose.png') 
CODE_BLOCKS = os.path.join(PATH, '..', 'assets', 'images') # Trim off the type and .png 



