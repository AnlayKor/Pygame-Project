import pygame
import sys

from player import Player
from wall import Wall
from start_screen import StartScreen


class Game:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 800, 500
        self.screen = pygame.display.set_mode(self.size)

        self.open_start_screen()

        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self, self.width // 2, self.height // 2, self.all_sprites)

        self.walls = []
        self.walls.append(Wall(self, 200, 100, 200, 50, self.all_sprites))
        self.walls.append(Wall(self, 300, 400, 50, 50, self.all_sprites))

        self.running = True
        self.clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                for sprite in self.all_sprites:
                    sprite.event(event)

            self.update(self.clock.tick(60))

            self.draw()
            pygame.display.flip()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def draw(self):
        self.screen.fill((50, 50, 50))
        self.draw_bg()
        self.all_sprites.draw(self.screen)

    def draw_bg(self):
        size = 20
        for i in range(0, self.screen.get_width(), size):
            for j in range(0, self.screen.get_height(), size):
                if i % (size * 2):
                    if j % (size * 2):
                        color = '#494949'
                    else:
                        color = '#3a3a3a'
                else:
                    if j % (size * 2):
                        color = '#3a3a3a'
                    else:
                        color = '#494949'
                rect = (i, j, size, size)
                pygame.draw.rect(self.screen, color, rect)

    def update(self, frame_time):
        delta = frame_time / 1000
        self.all_sprites.update(delta)

    def open_start_screen(self):
        StartScreen(self)


if __name__ == "__main__":
    game = Game()
