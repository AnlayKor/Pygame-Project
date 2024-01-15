import pygame
import math

from animated_sprite import AnimatedSprite


class Boom(AnimatedSprite):
    image = None

    def __init__(self, level, x, y, *groups):
        Boom.image = pygame.transform.scale_by(self.load_image('boom.png'), 6)

        self.level = level
        super().__init__(level.game, Boom.image, 2, 3, *groups)

        self.rect.center = x, y
        self.x = self.rect.x
        self.y = self.rect.y

        self.animation_fps = 16
        self.time_before_next_frame = 1

    def remove(self):
        for i, effect in enumerate(self.level.effects):
            if effect.rect == self.rect:
                del self.level.effects[i]
        self.game.effects.remove(self)
        self.game.all_sprites.remove(self)

    def update(self, delta):
        self.time_before_next_frame -= self.animation_fps * delta
        if self.time_before_next_frame <= 0:
            self.time_before_next_frame = 1
            self.cur_frame = self.cur_frame + 1
        if self.cur_frame < len(self.frames):
            self.image = self.frames[self.cur_frame]
        else:
            self.remove()

    def event(self, event: pygame.event.Event):
        pass
