import pygame
import math

from animated_sprite import AnimatedSprite
from barrel import Barrel
from crate import Crate
from wall import Wall
from enemy import Enemy


class One(Enemy):
    image = None
    default_health = 30

    def __init__(self, level, x, y, *groups):
        One.image = pygame.transform.scale_by(self.load_image('one.png'), 3)

        self.level = level
        super().__init__(level.game, One.image, 2, 1, *groups)

        self.rect.topleft = x, y
        self.x = self.rect.x
        self.y = self.rect.y

        self.health = One.default_health

        self.speed = 60
        self.x_direction = 0
        self.y_direction = 0

        self.animation_fps = 8
        self.time_before_next_frame = 1

        self.damage = 30
        self.attack_speed = 1
        self.attack_range = 50
        self.time_before_next_attack = 1

    def update(self, delta):
        self.time_before_next_frame -= self.animation_fps * delta
        if self.time_before_next_frame <= 0:
            self.time_before_next_frame = 1
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

        # move towards the player

        relative_x = self.level.player.x - self.x
        relative_y = self.level.player.y - self.y
        angle = math.atan2(relative_y, relative_x)

        self.x_direction = math.cos(angle)
        self.y_direction = math.sin(angle)

        self.move(self.x_direction * self.speed * delta,
                  self.y_direction * self.speed * delta)

        # attacking player

        if self.time_before_next_attack > 0:
            self.time_before_next_attack -= self.attack_speed * delta

        if abs(relative_x) + abs(relative_y) <= self.attack_range:
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
        if x_speed < 0:
            i = pygame.rect.Rect(self.rect.left + x_speed, self.rect.top, 1, self.rect.h).collidelist(self.level.walls)
            if i != -1:
                wall: Wall = self.level.walls[i]
                x_speed = wall.rect.right - self.rect.left
            if self.rect.left > 0:
                self.x += x_speed
            else:
                self.rect.left = 0
                self.x = self.rect.x
        if x_speed > 0:
            i = pygame.rect.Rect(self.rect.right + x_speed, self.rect.top, 1, self.rect.h).collidelist(self.level.walls)
            if i != -1:
                wall: Wall = self.level.walls[i]
                x_speed = wall.rect.left - self.rect.right
            if self.rect.right < self.game.width:
                self.x += x_speed
            else:
                self.rect.right = self.game.width
                self.x = self.rect.x
        if y_speed < 0:
            i = pygame.rect.Rect(self.rect.left, self.rect.top + y_speed, self.rect.w, 1).collidelist(self.level.walls)
            if i != -1:
                wall: Wall = self.level.walls[i]
                y_speed = wall.rect.bottom - self.rect.top
            if self.rect.top > 0:
                self.y += y_speed
            else:
                self.rect.top = 0
                self.y = self.rect.y
        if y_speed > 0:
            i = pygame.rect.Rect(self.rect.left, self.rect.bottom + y_speed, self.rect.w, 1).collidelist(self.level.walls)
            if i != -1:
                wall: Wall = self.level.walls[i]
                y_speed = wall.rect.top - self.rect.bottom
            if self.rect.bottom < self.game.height:
                self.y += y_speed
            else:
                self.rect.bottom = self.game.height
                self.y = self.rect.y

        self.rect.x = self.x
        self.rect.y = self.y
