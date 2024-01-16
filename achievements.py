import pygame

from sqlite3 import *


class Achievements:
    def __init__(self, game):
        game.screen.fill((0, 0, 0))

        font_name = pygame.font.Font(None, 70)
        font = pygame.font.Font(None, 55)
        font2 = pygame.font.Font(None, 40)
        font3 = pygame.font.Font(None, 20)

        color1 = pygame.color.Color('red')
        color2 = pygame.color.Color('white')

        text = font_name.render('Ваши достижения', True, color1)
        text_x = game.width // 2 - text.get_width() // 2
        text_y = 30
        game.screen.blit(text, (text_x, text_y))

        pygame.draw.line(game.screen, color2, (20, game.height - 20 - (game.height - 20 - text_y - text.get_height() - 30) / 3 * 2),
                         (game.width - 22, game.height - 20 - (game.height - 20 - text_y - text.get_height() - 30) / 3 * 2), 4)
        pygame.draw.line(game.screen, color2,
                         (20, game.height - 20 - (game.height - 20 - text_y - text.get_height() - 30) / 3),
                         (game.width - 22,
                          game.height - 20 - (game.height - 20 - text_y - text.get_height() - 30) / 3), 4)
        pygame.draw.rect(game.screen, color1, (20, text_y + text.get_height() + 30,
                                               game.width - 40, game.height - 20 - text_y - text.get_height() - 30), 4)
        pygame.draw.line(game.screen, color1, (20 + (game.width - 40) / 4, text_y + text.get_height() + 30),
                         (20 + (game.width - 40) / 4, game.height - 22), 4)
        pygame.draw.line(game.screen, color1, (20 + (game.width - 40) / 2, text_y + text.get_height() + 30),
                         (20 + (game.width - 40) / 2, game.height - 22), 4)
        pygame.draw.line(game.screen, color1, (20 + (game.width - 40) / 4 * 3, text_y + text.get_height() + 30),
                         (20 + (game.width - 40) / 4 * 3, game.height - 22), 4)

        y = text_y + text.get_height() + 30

        text1 = font2.render('Уровень', True, color2)
        text1_x = 20 + (game.width - 40) // 4 // 2 - text1.get_width() // 2
        text1_y = y + (game.height - 20 - text_y - text.get_height() - 30) // 6 - text1.get_height() // 2
        game.screen.blit(text1, (text1_x, text1_y))
        text2 = font2.render('сложности', True, color2)
        text2_x = 20 + (game.width - 40) // 4 // 2 - text2.get_width() // 2
        text2_y = text1_y + text1.get_height() + 10
        game.screen.blit(text2, (text2_x, text2_y))

        text3 = font2.render('Лучший', True, color2)
        text3_x = 20 + (game.width - 40) // 2 - (game.width - 40) // 8 - text3.get_width() // 2
        text3_y = y + (game.height - 20 - text_y - text.get_height() - 30) // 6 - text3.get_height() // 2
        game.screen.blit(text3, (text3_x, text3_y))
        text4 = font2.render('результат', True, color2)
        text4_x = 20 + (game.width - 40) // 2 - (game.width - 40) // 8 - text4.get_width() // 2
        text4_y = text3_y + text3.get_height() + 10
        game.screen.blit(text4, (text4_x, text4_y))

        text5 = font2.render('Среднее', True, color2)
        text5_x = 20 + (game.width - 40) // 4 * 3 - (game.width - 40) // 8 - text5.get_width() // 2
        text5_y = y + (game.height - 20 - text_y - text.get_height() - 30) // 6 - text5.get_height() // 2
        game.screen.blit(text5, (text5_x, text5_y))
        text6 = font2.render('время', True, color2)
        text6_x = 20 + (game.width - 40) // 4 * 3 - (game.width - 40) // 8 - text6.get_width() // 2
        text6_y = text5_y + text5.get_height() + 10
        game.screen.blit(text6, (text6_x, text6_y))

        text7 = font2.render('Количество', True, color2)
        text7_x = 20 + (game.width - 40) - (game.width - 40) // 8 - text7.get_width() // 2
        text7_y = y + (game.height - 20 - text_y - text.get_height() - 30) // 6 - text7.get_height() // 2
        game.screen.blit(text7, (text7_x, text7_y))
        text8 = font2.render('прохождений', True, color2)
        text8_x = 20 + (game.width - 40) - (game.width - 40) // 8 - text8.get_width() // 2
        text8_y = text7_y + text7.get_height() + 10
        game.screen.blit(text8, (text8_x, text8_y))

        text9 = font2.render('Средний', True, color2)
        text9_x = 20 + (game.width - 40) // 4 // 2 - text9.get_width() // 2
        text9_y = y + (game.height - 20 - text_y - text.get_height() - 30) // 2 - text9.get_height() // 2
        game.screen.blit(text9, (text9_x, text9_y))

        text10 = font2.render('Сложный', True, color2)
        text10_x = 20 + (game.width - 40) // 4 // 2 - text10.get_width() // 2
        text10_y = y + (game.height - 20 - text_y - text.get_height() - 30) // 6 * 5 - text10.get_height() // 2
        game.screen.blit(text10, (text10_x, text10_y))


        con = connect('data/Achievements.db')
        cur = con.cursor()
        seconds = cur.execute(f'''SELECT seconds FROM achievements WHERE complexity = 0''').fetchall()
        seconds0 = []
        for i in range(len(seconds)):
            seconds0.append(seconds[i][0])
        seconds = cur.execute(f'''SELECT seconds FROM achievements WHERE complexity = 1''').fetchall()
        seconds1 = []
        for i in range(len(seconds)):
            seconds1.append(seconds[i][0])
        con.close()

        try:
            best0 = min(seconds0)
            best0 = f'{best0 // 60 // 60}ч{best0 // 60 % 60}м{best0 % 60}c'
            average0 = round(sum(seconds0) / len(seconds0))
            average0 = f'{average0 // 60 // 60}ч{average0 // 60 % 60}м{average0 % 60}c'
        except Exception:
            best0 = ''
            average0 = ''
        try:
            best1 = min(seconds1)
            best1 = f'{best1 // 60 // 60}ч{best1 // 60 % 60}м{best1 % 60}c'
            average1 = round(sum(seconds1) / len(seconds1))
            average1 = f'{average1 // 60 // 60}ч{average1 // 60 % 60}м{average1 % 60}c'
        except Exception:
            best1 = ''
            average1 = ''
        count0 = str(len(seconds0))
        count1 = str(len(seconds1))

        text11 = font.render(best0, True, color1)
        text11_x = 20 + (game.width - 40) // 2 - (game.width - 40) // 8 - text11.get_width() // 2
        text11_y = y + (game.height - 20 - text_y - text.get_height() - 30) // 2 - text11.get_height() // 2
        game.screen.blit(text11, (text11_x, text11_y))

        text12 = font.render(best1, True, color1)
        text12_x = 20 + (game.width - 40) // 2 - (game.width - 40) // 8 - text12.get_width() // 2
        text12_y = y + (game.height - 20 - text_y - text.get_height() - 30) // 6 * 5 - text12.get_height() // 2
        game.screen.blit(text12, (text12_x, text12_y))

        text13 = font.render(average0, True, color1)
        text13_x = 20 + (game.width - 40) // 2 + (game.width - 40) // 8 - text13.get_width() // 2
        text13_y = y + (game.height - 20 - text_y - text.get_height() - 30) // 2 - text13.get_height() // 2
        game.screen.blit(text13, (text13_x, text13_y))

        text14 = font.render(average1, True, color1)
        text14_x = 20 + (game.width - 40) // 2 + (game.width - 40) // 8 - text14.get_width() // 2
        text14_y = y + (game.height - 20 - text_y - text.get_height() - 30) // 6 * 5 - text14.get_height() // 2
        game.screen.blit(text14, (text14_x, text14_y))

        text15 = font.render(count0, True, color1)
        text15_x = 20 + (game.width - 40) - (game.width - 40) // 8 - text15.get_width() // 2
        text15_y = y + (game.height - 20 - text_y - text.get_height() - 30) // 2 - text15.get_height() // 2
        game.screen.blit(text15, (text15_x, text15_y))

        text16 = font.render(count1, True, color1)
        text16_x = 20 + (game.width - 40) - (game.width - 40) // 8 - text16.get_width() // 2
        text16_y = y + (game.height - 20 - text_y - text.get_height() - 30) // 6 * 5 - text16.get_height() // 2
        game.screen.blit(text16, (text16_x, text16_y))

        text17 = font3.render('Нажмите enter для перехода на главное окно', True, color2)
        text17_x = game.width - 20 - text17.get_width()
        text17_y = game.height - 15
        game.screen.blit(text17, (text17_x, text17_y))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.terminate()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game.open_start_screen()
                        running = False
            pygame.display.flip()
