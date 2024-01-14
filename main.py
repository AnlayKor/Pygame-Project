import pygame
import sys

from player import Player
from wall import Wall
from start_screen import StartScreen
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.character = None
        self.player = None

        self.all_sprites = None
        self.floors = None
        self.walls = None
        self.entities = None
        self.reset_sprites()

        self.size = self.width, self.height = 60 * 14, 60 * 9
        self.screen = pygame.display.set_mode(self.size)

        self.open_start_screen()

        self.running = True
        self.clock = pygame.time.Clock()

        self.start()

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
        self.screen.fill((20, 20, 20))
        self.draw_bg()

        self.floors.draw(self.screen)
        self.walls.draw(self.screen)
        self.entities.draw(self.screen)

        if self.character == 'anton':
            self.display_name('Антон')
        if self.character == 'vika':
            self.display_name('Вика')

    def display_name(self, name):
        font = pygame.font.Font(None, 20)
        text = font.render(name, True, 'white')
        text_x = self.player.rect.width // 2 - text.get_width() // 2 + self.player.rect.x
        text_y = self.player.rect.y + self.player.rect.height + 10

        s = pygame.Surface((text.get_width() + 8, text.get_height() + 6))
        s.set_alpha(128)
        s.fill('black')
        self.screen.blit(s, (text_x - 4, text_y - 3))

        self.screen.blit(text, (text_x, text_y))

    def reset_sprites(self):
        self.all_sprites = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()

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

    def start(self):
        Level(self)


if __name__ == "__main__":
    game = Game()
