import pygame

from sprite import Sprite


class Door(Sprite):
    image = None

    def __init__(self, level, x, y, width, height, *groups):
        Door.image = pygame.transform.scale(self.load_image('door.png'), (width, height))
        super().__init__(level.game, Door.image, *groups)
        self.level = level
        self.rect.topleft = x, y
        self.x = self.rect.x
        self.y = self.rect.y
        self.used = False

    def update(self, delta):
        if not self.used:
            if self.level.player.rect.collidepoint(self.rect.center):
                self.level.next_room()
                self.used = True

    def event(self, event: pygame.event.Event):
        pass
