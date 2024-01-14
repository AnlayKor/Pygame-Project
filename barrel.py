import pygame

from sprite import Sprite


class Barrel(Sprite):
    image = None

    def __init__(self, level, x, y, width, height, *groups):
        Barrel.image = pygame.transform.scale(self.load_image('barrel.png'), (width, height))
        super().__init__(level.game, Barrel.image, *groups)
        self.rect.topleft = x, y
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self, delta):
        pass

    def event(self, event: pygame.event.Event):
        pass
