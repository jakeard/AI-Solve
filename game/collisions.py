import arcade
from game.player import Player

class Collisions:
    def execute(self, sprites):
        self.players = sprites['players']
        self.enemies = sprites['enemies']

        dead_list = self.check_enemy_collision()
        dead_list = self.check_fall(dead_list)
        return dead_list
    
    def check_enemy_collision(self):
        dead = []
        for player in self.players:
            for enemy in self.enemies:
                if player.collides_with_sprite(enemy):
                    moves, location = player.store_info()
                    self.players.remove(player)
                    dead.append((moves, location))
        return dead
    
    def check_fall(self, dead):
        for player in self.players:
            if player.center_y < 50:
                moves, location = player.store_info()
                self.players.remove(player)
                dead.append((moves, location))
        return dead