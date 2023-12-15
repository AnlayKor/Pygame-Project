import pygame


class StartScreen:
    def __init__(self, game):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.terminate()

            pygame.display.flip()
