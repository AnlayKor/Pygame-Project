import math
import pygame

from sprite import Sprite


class AnimatedSprite(Sprite):
    def __init__(self, game, image, columns, rows, *groups):
        super().__init__(game, image, *groups)
        self.frames = []
        self.cut_sheet(image, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))