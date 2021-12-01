import arcade
from game.player import Player

class Collisions:
    # collisions class handles player collisions with enemies, 
    # the flag, and if they have fallen out of the world
    def execute(self, sprites):
        self.players = sprites['players']
        self.enemies = sprites['enemies']
        self.flag = sprites['flag']

        dead_list = self.check_enemy_collision()
        dead_list = self.check_fall(dead_list)
        dead_or_won = self.won(dead_list)
        return dead_or_won
    
    def check_enemy_collision(self):
        # checks if any player has collided with an enemy
        dead = []
        for player in self.players:
            for enemy in self.enemies:
                if player.collides_with_sprite(enemy):
                    moves, location = player.store_info()
                    self.players.remove(player)
                    dead.append((moves, location))
        return dead
    
    def check_fall(self, dead):
        # checks if any player has fallen of of the level
        for player in self.players:
            if player.center_y < 50:
                moves, location = player.store_info()
                self.players.remove(player)
                dead.append((moves, location))
        return dead
    
    def won(self, dead):
        # checks if any player has collided with the flag, which would mean they have won
        for player in self.players:
            if player.collides_with_sprite(self.flag[0]):
                return True
        return dead