import pygame
from sprite import Sprite


class StartScreen(Sprite):
    def __init__(self, game, *groups):
        fon = pygame.transform.scale(self.load_image('fon.png'), (game.width, game.height))
        super().__init__(game, fon, *groups)
        game.screen.blit(fon, (0, 0))

        color2 = pygame.color.Color('red')
        color3 = pygame.color.Color('red')

        f2 = False
        f3 = False

        font_name = pygame.font.Font(None, 60)

        font = pygame.font.Font(None, 40)

        text = font_name.render('LMS Attack', True, 'red')
        text_x = 100
        text_y = 175
        game.screen.blit(text, (text_x, text_y))

        pygame.draw.line(game.screen, 'red',
                         (20, 75), (375, 75), 10)

        running = True
        while running:
            text2 = font.render('Начать игру', True, color2)
            text2_x = text.get_width() // 2 - text2.get_width() // 2 + text_x
            text2_y = 300
            game.screen.blit(text2, (text2_x, text2_y))

            pygame.draw.rect(game.screen, color2, (text2_x - 20, text2_y - 20,
                                                   text2.get_width() + 40, text2.get_height() + 40), 2)

            text3 = font.render('Достижения', True, color3)
            text3_x = text.get_width() // 2 - text3.get_width() // 2 + text_x
            text3_y = 400
            game.screen.blit(text3, (text3_x, text3_y))

            pygame.draw.rect(game.screen, color3, (text3_x - 20, text3_y - 20,
                                                   text3.get_width() + 40, text3.get_height() + 40), 2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.terminate()
                if event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = event.pos
                    if (mouse_x > text2_x - 20) and (mouse_x < text2_x - 20 + text2.get_width() + 40) and (
                            mouse_y > text2_y - 20) and (mouse_y < text2_y - 20 + text2.get_height() + 40):
                        color2.hsva = color2.hsva[0], color2.hsva[1], 50, color2.hsva[3]
                        f2 = True
                    else:
                        color2 = pygame.color.Color('red')
                        f2 = False
                    if (mouse_x > text3_x - 20) and (mouse_x < text3_x - 20 + text3.get_width() + 40) and (
                            mouse_y > text3_y - 20) and (mouse_y < text3_y - 20 + text3.get_height() + 40):
                        color3.hsva = color3.hsva[0], color3.hsva[1], 50, color3.hsva[3]
                        f3 = True
                    else:
                        color3 = pygame.color.Color('red')
                        f3 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if f2:
                            running = False
                        elif f3:
                            pass
            pygame.display.flip()
