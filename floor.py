import pygame

from sprite import Sprite


class Floor(Sprite):
    image = None

    def __init__(self, level, x, y, width, height, *groups):
        Floor.image = pygame.transform.scale(self.load_image(level.get_floor()), (width, height))
        super().__init__(level.game, Floor.image, *groups)
        self.rect.topleft = x, y
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self, delta):
        pass

    def event(self, event: pygame.event.Event):
        pass
