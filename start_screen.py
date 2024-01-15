import pygame
from sprite import Sprite
from character_choice import CharacterChoice


class StartScreen(Sprite):
    def __init__(self, game, *groups):
        fon = pygame.transform.scale(self.load_image('fon.png'), (game.width, game.height))
        super().__init__(game, fon, *groups)
        game.screen.blit(fon, (0, 0))

        color2 = pygame.color.Color('red')
        color3 = pygame.color.Color('red')

        flag_button2 = False
        flag_button3 = False

        font_name = pygame.font.Font(None, 80)

        font = pygame.font.Font(None, 40)

        text = font_name.render('LMS Attack', True, 'red')
        text_x = 50
        text_y = 175
        game.screen.blit(text, (text_x, text_y))

        pygame.draw.line(game.screen, 'red',
                         (20, 80), (385, 80), 10)

        pygame.draw.rect(game.screen, 'black',
                         (20, 455, 65, 70))

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
                        flag_button2 = True
                    else:
                        color2 = pygame.color.Color('red')
                        flag_button2 = False
                    if (mouse_x > text3_x - 20) and (mouse_x < text3_x - 20 + text3.get_width() + 40) and (
                            mouse_y > text3_y - 20) and (mouse_y < text3_y - 20 + text3.get_height() + 40):
                        color3.hsva = color3.hsva[0], color3.hsva[1], 50, color3.hsva[3]
                        flag_button3 = True
                    else:
                        color3 = pygame.color.Color('red')
                        flag_button3 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if flag_button2:
                            self.open_character_choice()
                            running = False
                        elif flag_button3:
                            pass
            pygame.display.flip()

    def open_character_choice(self):
        CharacterChoice(self.game)
