import pygame

from sprite import Sprite


class Barrel(Sprite):
    image = None

    def __init__(self, level, x, y, width, height, *groups):
        Barrel.image = pygame.transform.scale(self.load_image('barrel.png'), (width, height))
        super().__init__(level.game, Barrel.image, *groups)
        self.level = level
        self.rect.topleft = x, y
        self.x = self.rect.x
        self.y = self.rect.y

    def remove(self):
        for i, wall in enumerate(self.level.walls):
            if wall.rect == self.rect:
                del self.level.walls[i]
        self.game.walls.remove(self)
        self.game.all_sprites.remove(self)

    def blow_up(self):
        self.remove()

    def update(self, delta):
        i = self.rect.collidelist(self.level.projectiles)
        if i != -1:
            self.level.projectiles[i].remove()
            self.remove()

    def event(self, event: pygame.event.Event):
        pass
