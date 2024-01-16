import pygame

from animated_sprite import AnimatedSprite
from barrel import Barrel
from crate import Crate


class DarinaSword(AnimatedSprite):
    image = None

    def __init__(self, level, player, *groups):
        DarinaSword.image = pygame.transform.scale_by(self.load_image('swordanim.png'), 1 / 4)
        super().__init__(level.game, DarinaSword.image, 1, 5, *groups)
        self.level = level
        self.level.weapons.append(self)
        self.player = player
        self.rect.center = player.rect.center
        self.x = self.rect.x
        self.y = self.rect.y

        self.animation_fps = 24
        self.time_before_next_frame = 1

        self.attacking = False
        self.flipping = False

        self.attack_range = 130
        self.attack_speed = 2
        self.time_before_next_attack = 0

        if level.game.character == 'anton':
            self.damage = 9
        else:
            self.damage = 15

    def update(self, delta):
        self.rect.center = self.player.rect.center
        self.x = self.rect.x
        self.y = self.rect.y

        if self.time_before_next_attack > 0:
            self.time_before_next_attack -= self.attack_speed * delta

        if self.attacking:
            self.time_before_next_frame -= self.animation_fps * delta
            if self.time_before_next_frame <= 0:
                self.time_before_next_frame = 1
                self.cur_frame = self.cur_frame + 1
            if self.cur_frame == len(self.frames):
                self.cur_frame = 0
                self.attacking = False
        if self.flipping:
            self.image = pygame.transform.flip(self.frames[self.cur_frame], 1, 0)
        else:
            self.image = self.frames[self.cur_frame]

    def attack(self):
        if self.time_before_next_attack > 0:
            return
        self.time_before_next_attack = 1
        self.attacking = True

    def remove(self):
        for i, weapon in enumerate(self.level.weapons):
            if weapon.rect == self.rect:
                del self.level.weapons[i]
        self.game.weapons.remove(self)
        self.game.all_sprites.remove(self)

    def event(self, event: pygame.event.Event):
        pass
