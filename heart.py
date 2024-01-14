import pygame

from sprite import Sprite


class Heart(Sprite):
    image = None

    def __init__(self, level, x, y, width, height, *groups):
        Heart.image = pygame.transform.scale(self.load_image('heart.png'), (width, height))
        super().__init__(level.game, Heart.image, *groups)
        self.level = level
        self.rect.center = x, y
        self.x = self.rect.x
        self.y = self.rect.y

    def remove(self):
        for i, collectable in enumerate(self.level.collectables):
            if collectable.rect == self.rect:
                del self.level.collectables[i]
        self.game.collectables.remove(self)
        self.game.all_sprites.remove(self)

    def update(self, delta):
        if self.rect.colliderect(self.level.player.rect):
            self.level.player.heal(1)
            self.remove()

    def event(self, event: pygame.event.Event):
        pass
