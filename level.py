import pygame
import csv
import os

from player import Player
from wall import Wall
from floor import Floor
from door import Door


class Level:
    def __init__(self, game):
        self.wall = None
        self.floor = None
        self.player = None
        self.door = None

        self.level = None
        self.room = 1

        self.game = game
        self.walls = []
        self.floors = []
        self.tile_size = 60

    def get_wall(self):
        return self.wall

    def get_floor(self):
        return self.floor

    def load_room(self, room):
        room = f'room{room}.csv'
        with open(os.path.join('data/levels/', self.level, room)) as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            for i, row in enumerate(reader):
                for j, tile in enumerate(row):
                    if tile in '0PD':
                        floor = Floor(self, j * self.tile_size, i * self.tile_size,
                                      self.tile_size, self.tile_size, self.game.floors)
                        self.floors.append(floor)
                    if tile == 'W':
                        wall = Wall(self, j * self.tile_size, i * self.tile_size,
                                    self.tile_size, self.tile_size, self.game.walls)
                        self.walls.append(wall)
                    if tile == 'P':
                        self.player = Player(self, j * self.tile_size, i * self.tile_size, self.game.entities)
                    if tile == 'D':
                        self.door = Door(self, j * self.tile_size, i * self.tile_size,
                                         self.tile_size, self.tile_size, self.game.walls)

    def clear_room(self):
        self.walls = []
        self.floors = []
        self.player = None
        self.door = None

        self.game.reset_sprites()

    def next_room(self):
        self.clear_room()
        self.room += 1
        self.load_room(self.room)
