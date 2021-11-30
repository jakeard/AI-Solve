import arcade
from game.player import Player

class Collisions:
    def execute(self, sprites):
        self.players = sprites['players']
        self.enemies = sprites['enemies']

        x = self.check_enemy_collision()
        # return self._check_enemy_collision()
        return x
    
    def check_enemy_collision(self):
        dead = []
        for player in self.players:
            for enemy in self.enemies:
                if player.collides_with_sprite(enemy):
                    moves, location = player.store_info()
                    self.players.remove(player)
                    dead.append((moves, location))
        return dead
