import arcade
from game import constants
from game.director import Director


def main():
    # starts the program
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    view = Director()
    view.setup()
    window.show_view(view)
    arcade.run()


if __name__ == "__main__":
    main()