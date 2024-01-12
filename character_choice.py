import pygame
from sprite import Sprite


class CharacterChoice(Sprite):
    def __init__(self, game, *groups):
        anton = pygame.transform.scale(self.load_image('anton.png'), (200, 200))
        vika = pygame.transform.scale(self.load_image('vika.png'), (200, 200))
        noname = pygame.transform.scale(self.load_image('player.png'), (200, 200))
        super().__init__(game, anton, *groups)
        game.screen.fill((0, 0, 0))

        stealth_color1 = pygame.color.Color((0, 0, 0))
        stealth_color2 = pygame.color.Color((25, 25, 25))
        stealth_color3 = pygame.color.Color((25, 25, 25))
        color2 = pygame.color.Color('red')
        color3 = pygame.color.Color('red')

        f1 = False
        f2 = False
        f3 = False

        font_name = pygame.font.Font(None, 60)
        font = pygame.font.Font(None, 40)
        stealth_font = pygame.font.Font(None, 35)

        text = font_name.render('Выберите уровень сложности', True, 'red')
        text_x = game.width // 2 - text.get_width() // 2
        text_y = 40
        game.screen.blit(text, (text_x, text_y))

        running = True
        while running:
            noname_x = game.width // 3 // 2 - noname.get_width() // 2
            noname_y = 80 + text.get_height()
            game.screen.blit(noname, (noname_x, noname_y))

            pygame.draw.rect(game.screen, 'red', (noname_x, noname_y,
                                                   noname.get_width(), noname.get_height()), 4)

            anton_x = game.width // 3 * 2 + game.width // 3 // 2 - anton.get_width() // 2
            anton_y = 80 + text.get_height()
            game.screen.blit(anton, (anton_x, anton_y))

            pygame.draw.rect(game.screen, color3, (anton_x, anton_y,
                                                   anton.get_width(), anton.get_height()), 4)

            vika_x = game.width // 2 - vika.get_width() // 2
            vika_y = 80 + text.get_height()
            game.screen.blit(vika, (vika_x, vika_y))

            pygame.draw.rect(game.screen, color2, (vika_x, vika_y,
                                                   vika.get_width(), vika.get_height()), 4)

            text1 = font.render('Лёгкий(?????)', True, 'red')
            text1_x = noname.get_width() // 2 - text1.get_width() // 2 + noname_x
            text1_y = noname_y + noname.get_height() + 10
            game.screen.blit(text1, (text1_x, text1_y))

            text2 = font.render('Средний(Вика)', True, 'red')
            text2_x = vika.get_width() // 2 - text2.get_width() // 2 + vika_x
            text2_y = vika_y + vika.get_height() + 10
            game.screen.blit(text2, (text2_x, text2_y))

            text3 = font.render('Сложный(Антон)', True, 'red')
            text3_x = anton.get_width() // 2 - text2.get_width() // 2 + anton_x
            text3_y = anton_y + anton.get_height() + 10
            game.screen.blit(text3, (text3_x, text3_y))

            stealth_text1 = stealth_font.render('Легко в этой игре не бывает!', True, stealth_color1)
            stealth_text1_x = game.width // 2 - stealth_text1.get_width() // 2
            stealth_text1_y = text2_y + text2.get_height() + 10
            game.screen.blit(stealth_text1, (stealth_text1_x, stealth_text1_y))

            stealth_text2 = stealth_font.render('Средняя девочка + средние способности = средняя сложность', True, stealth_color2)
            stealth_text2_x = game.width // 2 - stealth_text2.get_width() // 2
            stealth_text2_y = stealth_text1_y + stealth_text1.get_height() + 10
            game.screen.blit(stealth_text2, (stealth_text2_x, stealth_text2_y))

            stealth_text3 = stealth_font.render('Примитивные боевые способности Антона', True, stealth_color3)
            stealth_text3_x = game.width // 2 - stealth_text3.get_width() // 2
            stealth_text3_y = stealth_text2_y + stealth_text2.get_height() + 10
            game.screen.blit(stealth_text3, (stealth_text3_x, stealth_text3_y))

            stealth_text4 = stealth_font.render('и повышенная агрессивнсть монстров усложняют игру', True, stealth_color3)
            stealth_text4_x = game.width // 2 - stealth_text4.get_width() // 2
            stealth_text4_y = stealth_text3_y + stealth_text3.get_height() + 10
            game.screen.blit(stealth_text4, (stealth_text4_x, stealth_text4_y))

            if f1:
                pygame.draw.line(game.screen, 'red',
                                 (noname_x + 4, noname_y + 4), (noname_x + noname.get_width() - 4,
                                                        noname_y + noname.get_height() - 4), 6)
                pygame.draw.line(game.screen, 'red',
                                 (noname_x + 4, noname_y + noname.get_height() - 4), (noname_x + noname.get_width() - 4,
                                                                noname_y + 4), 6)
                stealth_color1 = pygame.color.Color((255, 0, 0))
            else:
                stealth_color1 = pygame.color.Color((0, 0, 0))

            if f2:
                stealth_color2 = pygame.color.Color((255, 0, 0))
            else:
                stealth_color2 = pygame.color.Color((0, 0, 0))

            if f3:
                stealth_color3 = pygame.color.Color((255, 0, 0))
            else:
                stealth_color3 = pygame.color.Color((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.terminate()
                if event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = event.pos
                    if (mouse_x > anton_x) and (mouse_x < anton_x + anton.get_width()) and (
                            mouse_y > anton_y) and (mouse_y < anton_y + anton.get_height()):
                        color3.hsva = color3.hsva[0], color3.hsva[1], 50, color3.hsva[3]
                        f3 = True
                    else:
                        color3 = pygame.color.Color('red')
                        f3 = False
                    if (mouse_x > vika_x) and (mouse_x < vika_x + vika.get_width()) and (
                            mouse_y > vika_y) and (mouse_y < vika_y + vika.get_height()):
                        color2.hsva = color2.hsva[0], color2.hsva[1], 50, color2.hsva[3]
                        f2 = True
                    else:
                        color2 = pygame.color.Color('red')
                        f2 = False
                    if (mouse_x > noname_x) and (mouse_x < noname_x + noname.get_width()) and (
                            mouse_y > noname_y) and (mouse_y < noname_y + noname.get_height()):
                        f1 = True
                    else:
                        f1 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if f2:
                            self.choose_character('vika')
                            running = False
                        elif f3:
                            self.choose_character('anton')
                            running = False
            pygame.display.flip()

    def choose_character(self, character):
        self.game.character = character
