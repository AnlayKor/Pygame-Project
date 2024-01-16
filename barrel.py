import pygame

from boom import Boom
from crate import Crate
from sprite import Sprite


class Barrel(Sprite):
    image = None

    def __init__(self, level, x, y, width, height, *groups):
        Barrel.image = pygame.transform.scale(self.load_image('barrel.png'), (width, height))
        super().__init__(level.game, Barrel.image, *groups)
        self.size = width
        self.level = level
        self.rect.topleft = x, y
        self.x = self.rect.x
        self.y = self.rect.y

        self.damage = 150

    def remove(self):
        for i, wall in enumerate(self.level.walls):
            if wall.rect == self.rect:
                del self.level.walls[i]
        self.game.walls.remove(self)
        self.game.all_sprites.remove(self)

    def blow_up(self):
        boom = Boom(self.level, self.rect.centerx, self.rect.centery, self.game.effects)
        self.level.effects.append(boom)

        self.remove()

        for i in range(self.rect.centerx - self.size, self.rect.centerx + self.size + 1, self.size):
            for j in range(self.rect.centery - self.size, self.rect.centery + self.size + 1, self.size):
                if i == self.rect.centerx and j == self.rect.centery:
                    continue
                for wall in self.level.walls:
                    if wall.rect.centerx == i and wall.rect.centery == j:
                        if type(wall) is Crate:
                            wall.remove()
                        if type(wall) is Barrel:
                            wall.remove()

        for enemy in self.level.enemies:
            if boom.rect.colliderect(enemy.rect):
                enemy.get_damage(self.damage)

        if boom.rect.colliderect(self.level.player.rect):
            self.level.player.get_damage(self.damage)

    def update(self, delta):
        i = self.rect.collidelist(self.level.projectiles)
        if i != -1:
            self.level.projectiles[i].remove()
            self.blow_up()

    def event(self, event: pygame.event.Event):
        pass
