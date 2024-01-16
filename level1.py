import pygame
from level import Level


class Level1(Level):
    def __init__(self, game):
        super().__init__(game)

        self.wall = 'wall1.png'
        self.floor = 'floor1.png'
        self.level = 'level1'

        self.load_room(self.room)
