import math
import pygame

from animated_sprite import AnimatedSprite
from wall import Wall


class Player(AnimatedSprite):
    image = None
    left_keys = (pygame.K_LEFT, pygame.K_a)
    right_keys = (pygame.K_RIGHT, pygame.K_d)
    up_keys = (pygame.K_UP, pygame.K_w)
    down_keys = (pygame.K_DOWN, pygame.K_s)

    def __init__(self, game, x, y, *groups):
        # Player.image = pygame.transform.scale(self.load_image('antonidle.png'), (80, 80))
        self.idle_image = None
        self.walk_image = None
        self.load_character_images(game.character)

        Player.image = self.idle_image
        super().__init__(game, Player.image, 1, 2, *groups)
        self.rect.center = x, y
        self.x = self.rect.x
        self.y = self.rect.y

        self.speed = 200
        self.x_direction = 0
        self.y_direction = 0

        self.idle_fps = 2
        self.walk_fps = 8
        self.animation_fps = self.idle_fps
        self.cur_animation = 'idle'
        self.time_before_next_frame = 1

        self.is_left = False

    def change_animation(self, animation):
        self.cur_frame = 0
        self.cur_animation = animation

        if animation == 'idle':
            image = self.idle_image
            self.cut_sheet(image, 1, 2)
            self.animation_fps = self.idle_fps
        if animation == 'walk':
            image = self.walk_image
            self.cut_sheet(image, 2, 2)
            self.animation_fps = self.walk_fps

    def load_character_images(self, character):
        if character == 'anton':
            self.idle_image = pygame.transform.scale_by(self.load_image('antonidle.png'), 4)
            self.walk_image = pygame.transform.scale_by(self.load_image('antonwalk.png'), 4)
        else:
            self.idle_image = pygame.transform.scale_by(self.load_image('vikaidle.png'), 4)
            self.walk_image = pygame.transform.scale_by(self.load_image('vikawalk.png'), 4)

    def update(self, delta):
        # getting player direction

        self.x_direction = self.y_direction = 0
        keys = pygame.key.get_pressed()

        if keys[self.left_keys[0]] or keys[self.left_keys[1]]:
            self.x_direction -= 1
        if keys[self.right_keys[0]] or keys[self.right_keys[1]]:
            self.x_direction += 1
        if keys[self.up_keys[0]] or keys[self.up_keys[1]]:
            self.y_direction -= 1
        if keys[self.down_keys[0]] or keys[self.down_keys[1]]:
            self.y_direction += 1

        if self.x_direction != 0:
            self.is_left = self.x_direction < 0


        # changing animation

        if self.x_direction or self.y_direction:
            if self.cur_animation != 'walk':
                self.change_animation('walk')
        elif self.cur_animation != 'idle':
            self.change_animation('idle')


        # changing animation frame

        self.time_before_next_frame -= self.animation_fps * delta
        if self.time_before_next_frame <= 0:
            self.time_before_next_frame = 1
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)

        # flip if player going left

        if self.is_left:
            self.image = pygame.transform.flip(self.frames[self.cur_frame], 1, 0)
        else:
            self.image = self.frames[self.cur_frame]


        # normalizing player's direction

        if self.x_direction and self.y_direction:
            self.x_direction /= math.sqrt(2)
            self.y_direction /= math.sqrt(2)


        # moving player

        self.move(self.x_direction * self.speed * delta,
                  self.y_direction * self.speed * delta)

    def move(self, x_speed, y_speed):
        if x_speed < 0:
            i = pygame.rect.Rect(self.rect.left + x_speed, self.rect.top, 1, self.rect.h).collidelist(self.game.walls)
            if i != -1:
                wall: Wall = self.game.walls[i]
                x_speed = wall.rect.right - self.rect.left
            if self.rect.left > 0:
                self.x += x_speed
            else:
                self.rect.left = 0
                self.x = self.rect.x
        if x_speed > 0:
            i = pygame.rect.Rect(self.rect.right + x_speed, self.rect.top, 1, self.rect.h).collidelist(self.game.walls)
            if i != -1:
                wall: Wall = self.game.walls[i]
                x_speed = wall.rect.left - self.rect.right
            if self.rect.right < self.game.width:
                self.x += x_speed
            else:
                self.rect.right = self.game.width
                self.x = self.rect.x
        if y_speed < 0:
            i = pygame.rect.Rect(self.rect.left, self.rect.top + y_speed, self.rect.w, 1).collidelist(self.game.walls)
            if i != -1:
                wall: Wall = self.game.walls[i]
                y_speed = wall.rect.bottom - self.rect.top
            if self.rect.top > 0:
                self.y += y_speed
            else:
                self.rect.top = 0
                self.y = self.rect.y
        if y_speed > 0:
            i = pygame.rect.Rect(self.rect.left, self.rect.bottom + y_speed, self.rect.w, 1).collidelist(self.game.walls)
            if i != -1:
                wall: Wall = self.game.walls[i]
                y_speed = wall.rect.top - self.rect.bottom
            if self.rect.bottom < self.game.height:
                self.y += y_speed
            else:
                self.rect.bottom = self.game.height
                self.y = self.rect.y

        self.rect.x = self.x
        self.rect.y = self.y

        # for i in self.rect.collidelistall(self.game.walls):
        #     wall: Wall = self.game.walls[i]
        #     if x_speed > 0 and self.rect.right > wall.rect.left:
        #         self.rect.right = wall.rect.left
        #     if x_speed < 0 and self.rect.left < wall.rect.right:
        #         self.rect.left = wall.rect.right
        #     if y_speed > 0 and self.rect.bottom > wall.rect.top:
        #         self.rect.bottom = wall.rect.top
        #     if y_speed < 0 and self.rect.top < wall.rect.bottom:
        #         self.rect.top = wall.rect.bottom
        #     self.x = self.rect.x
        #     self.y = self.rect.y




    # def get_walls_collisions(self, x_speed, y_speed):
    #     left = right = top = bottom = False
    #     for i in self.rect.collidelistall(self.game.walls):
    #         wall: Wall = self.game.walls[i]
    #         if wall.rect.right - x_speed >= self.rect.left:
    #             self.x = self.rect.left = wall.rect.right + 1
    #         if wall.rect.left - x_speed <= self.rect.right:
    #             right = True
    #         if wall.rect.bottom - y_speed >= self.rect.top:
    #             top = True
    #         if wall.rect.top - y_speed <= self.rect.bottom:
    #             bottom = True
    #     return left, right, top, bottom

    def event(self, event: pygame.event.Event):
        pass
