import pygame
import math

from animated_sprite import AnimatedSprite
from barrel import Barrel
from crate import Crate
from wall import Wall
from enemy import Enemy


class Snake(Enemy):
    image = None

    def __init__(self, level, x, y, direction, *groups):
        Snake.image = pygame.transform.scale_by(self.load_image('snake.png'), 3)

        self.level = level
        super().__init__(level.game, Snake.image, 1, 1, *groups)

        self.rect.topleft = x, y
        self.x = self.rect.x
        self.y = self.rect.y

        self.default_health = 30000
        if level.game.character == 'anton':
            self.default_health *= 2
        self.health = self.default_health

        self.speed = 600
        self.x_direction = direction

        self.animation_fps = 8
        self.time_before_next_frame = 1

        self.damage = 30
        if level.game.character == 'anton':
            self.damage *= 1.5
        self.attack_speed = 1
        self.attack_range = 50
        self.time_before_next_attack = 0

        self.time_before_change_direction = 2

        self.is_left = False

    def update(self, delta):
        self.is_left = self.x_direction < 0

        self.time_before_next_frame -= self.animation_fps * delta
        if self.time_before_next_frame <= 0:
            self.time_before_next_frame = 1
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)

        if self.is_left:
            self.image = pygame.transform.flip(self.frames[self.cur_frame], 1, 0)
        else:
            self.image = self.frames[self.cur_frame]

        # move towards the player

        self.move(self.x_direction * self.speed * delta,
                  0)

        # attacking player

        if self.time_before_next_attack > 0:
            self.time_before_next_attack -= self.attack_speed * delta

        if self.time_before_change_direction > 0:
            self.time_before_change_direction -= delta
        else:
            self.time_before_change_direction = 2.5
            self.x_direction *= -1
            self.rect.y += self.game.height / 2 - 100
            self.y = self.rect.y

        if self.rect.colliderect(self.level.player.rect):
            self.attack()

    def attack(self):
        if self.time_before_next_attack <= 0:
            self.time_before_next_attack = 1
            self.level.player.get_damage(self.damage)

        for wall in self.level.walls:
            if type(wall) is Crate or type(wall) is Barrel:
                relative_x = wall.rect.centerx - self.rect.centerx
                relative_y = wall.rect.centery - self.rect.centery

                if abs(relative_x) + abs(relative_y) <= self.attack_range * 1.5:
                    wall.remove()

    def event(self, event: pygame.event.Event):
        pass

    def move(self, x_speed, y_speed):
        self.x += x_speed
        self.y += y_speed

        self.rect.x = self.x
        self.rect.y = self.y
