import pygame

from animated_sprite import AnimatedSprite
from barrel import Barrel
from crate import Crate


class Stick(AnimatedSprite):
    image = None

    def __init__(self, level, player, *groups):
        Stick.image = pygame.transform.scale_by(self.load_image('stickanim.png'), 1/4)
        super().__init__(level.game, Stick.image, 1, 5, *groups)
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

        if level.game.character == 'anton':
            self.damage = 3
        else:
            self.damage = 5

    def update(self, delta):
        self.rect.center = self.player.rect.center
        self.x = self.rect.x
        self.y = self.rect.y

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
        self.attacking = True

        relative_x = self.player.rect.centerx - mouse_pos[0]
        relative_y = self.player.rect.centery - mouse_pos[1]

        if abs(relative_x) + abs(relative_y) <= self.attack_range:
            for wall in self.level.walls:
                if wall.rect.collidepoint(mouse_pos):
                    if type(wall) is Crate:
                        wall.remove()
                    if type(wall) is Barrel:
                        wall.blow_up()
            for enemy in self.level.enemies:
                if enemy.rect.collidepoint(mouse_pos):
                    enemy.get_damage(self.damage)

    def remove(self):
        for i, weapon in enumerate(self.level.weapons):
            if weapon.rect == self.rect:
                del self.level.weapons[i]
        self.game.weapons.remove(self)
        self.game.all_sprites.remove(self)

    def event(self, event: pygame.event.Event):
        pass
