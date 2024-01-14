import pygame
import csv
import os

from player import Player
from wall import Wall
from floor import Floor
from door import Door
from zero import Zero
from one import One
from bug import Bug
from barrel import Barrel
from crate import Crate


class Level:
    def __init__(self, game):
        self.wall = None
        self.floor = None
        self.player = None
        self.door = None

        self.level = 1
        self.room = 2

        self.game = game
        self.walls = []
        self.floors = []
        self.projectiles = []
        self.tile_size = 60

        self.load_room()

    def get_wall(self):
        return self.wall

    def get_floor(self):
        return self.floor

    def load_room(self):
        room = f'room{self.room}.csv'
        level = f'level{self.level}/'
        self.wall = f'wall{self.level}.png'
        self.floor = f'floor{self.level}.png'
        with open(os.path.join('data/levels/', level, room)) as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            for i, row in enumerate(reader):
                for j, tile in enumerate(row):
                    if tile not in 'W':
                        floor = Floor(self, j * self.tile_size, i * self.tile_size,
                                      self.tile_size, self.tile_size, self.game.floors)
                        self.floors.append(floor)
                    if tile == 'W':
                        wall = Wall(self, j * self.tile_size, i * self.tile_size,
                                    self.tile_size, self.tile_size, self.game.walls)
                        self.walls.append(wall)
                    if tile == 'C':
                        crate = Crate(self, j * self.tile_size, i * self.tile_size,
                                      self.tile_size, self.tile_size, self.game.walls)
                        self.walls.append(crate)
                    if tile == 'B':
                        barrel = Barrel(self, j * self.tile_size, i * self.tile_size,
                                        self.tile_size, self.tile_size, self.game.walls)
                        self.walls.append(barrel)
                    if tile == 'P':
                        self.player = Player(self, j * self.tile_size, i * self.tile_size, self.game.entities)
                        self.game.player = self.player
                    if tile == 'D':
                        self.door = Door(self, j * self.tile_size, i * self.tile_size,
                                         self.tile_size, self.tile_size, self.game.walls)
                    if tile == '0':
                        Zero(self, j * self.tile_size, i * self.tile_size, self.game.entities)
                    if tile == '1':
                        One(self, j * self.tile_size, i * self.tile_size, self.game.entities)
                    if tile == '2':
                        Bug(self, j * self.tile_size, i * self.tile_size, self.game.entities)

    def clear_room(self):
        self.walls = []
        self.floors = []
        self.player = None
        self.door = None

        self.game.reset_sprites()

    def next_room(self):
        self.clear_room()
        if self.room != 3:
           self.room += 1
        else:
            self.room = 1
            self.level += 1
        self.load_room()
