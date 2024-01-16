import math

import pygame

from animated_sprite import AnimatedSprite
from barrel import Barrel
from crate import Crate
from fireball import FireBall


class MagicStick(AnimatedSprite):
    image = None

    def __init__(self, level, player, *groups):
        MagicStick.image = pygame.transform.scale_by(self.load_image('magicstickanim.png'), 1/4)
        super().__init__(level.game, MagicStick.image, 1, 5, *groups)
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
        
        self.attack_range = 120
        self.attack_speed = 0.5
        self.time_before_next_attack = 0

        if level.game.character == 'anton':
            self.damage = 3
        else:
            self.damage = 5

    def spawn_fireball(self, mouse_pos):
        relative_x = mouse_pos[0] - self.rect.centerx
        relative_y = mouse_pos[1] - self.rect.centery
        angle = math.atan2(relative_y, relative_x)

        x_direction = math.cos(angle)
        y_direction = math.sin(angle)

        FireBall(self.level, self.rect.centerx, self.rect.centery, x_direction, y_direction, angle, self.level.game.projectiles)

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

    def attack(self, mouse_pos):
        if self.time_before_next_attack > 0:
            return
        self.time_before_next_attack = 1
        self.attacking = True

        self.spawn_fireball(mouse_pos)

    def remove(self):
        for i, weapon in enumerate(self.level.weapons):
            if weapon.rect == self.rect:
                del self.level.weapons[i]
        self.game.weapons.remove(self)
        self.game.all_sprites.remove(self)

    def event(self, event: pygame.event.Event):
        pass
