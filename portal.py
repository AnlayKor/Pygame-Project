import pygame

from sprite import Sprite


class Portal(Sprite):
    image = None

    def __init__(self, level, x, y, *groups):
        Portal.image = pygame.transform.scale(self.load_image('portal.png'), (100, 100))
        super().__init__(level.game, Portal.image, *groups)
        self.level = level
        self.rect.center = x, y
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
