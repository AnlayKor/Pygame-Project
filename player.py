import math
import pygame

from sprite import Sprite


class Player(Sprite):
    image = None

    def __init__(self, game, *groups):
        Player.image = pygame.transform.scale(self.load_image('player.png'), (50, 50))
        super().__init__(game, Player.image, *groups)

        self.x = game.width // 2
        self.y = game.height // 2
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 100
        self.angle = 0

    def update(self, delta):
        dx = pygame.mouse.get_pos()[0] - self.rect.centerx
        dy = pygame.mouse.get_pos()[1] - self.rect.centery
        distance = math.sqrt(dy ** 2 + dx ** 2)

        self.angle = math.degrees(math.atan2(-dy, dx))

        if distance > 3:
            self.rotate(Player.image, self.angle)
            self.x += math.cos(math.radians(self.angle)) * self.speed * delta
            self.y -= math.sin(math.radians(self.angle)) * self.speed * delta

        self.rect.centerx = self.x
        self.rect.centery = self.y

    def event(self, event: pygame.event.Event):
        pass
