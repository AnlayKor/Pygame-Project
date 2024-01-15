import pygame

from sqlite3 import *

from start_screen import StartScreen


class StartTitles:
    def __init__(self, game):

        game.screen.fill((0, 0, 0))

        time = (pygame.time.get_ticks() - game.time_start) // 1000
        sec = time % 60
        min = time // 60 % 60
        hour = time // 60 // 60

        if game.character == 'anton':
            difficulty_level = 'высокой сложности'
            complexity = 1
        else:
            difficulty_level = 'средней сложности'
            complexity = 0

        con = connect('data/Achievements.db')
        cur = con.cursor()
        cur.execute(f'INSERT INTO achievements (seconds, complexity) VALUES ({time}, {complexity})')
        con.commit()

        font_name = pygame.font.Font(None, 65)
        font = pygame.font.Font(None, 45)
        font2 = pygame.font.Font(None, 30)

        color1 = pygame.color.Color('red')
        color2 = pygame.color.Color('white')

        text = font_name.render('Поздравляем с завершением игры!', True, color2)
        text_x = game.width // 2 - text.get_width() // 2
        text_y = 80
        game.screen.blit(text, (text_x, text_y))

        text1 = font.render(f'Вы прошли уровень {difficulty_level} за {hour}ч{min}м{sec}с!', True, color1)
        text1_x = game.width // 2 - text1.get_width() // 2
        text1_y = 200
        game.screen.blit(text1, (text1_x, text1_y))

        text2 = font.render(f'Это обязательно отобразится в ваших достижениях', True, color2)
        text2_x = game.width // 2 - text2.get_width() // 2
        text2_y = 240
        game.screen.blit(text2, (text2_x, text2_y))

        text3 = font2.render(
            f'Нажмите enter для перехода на главное окно', True, color2)
        text3_x = 10
        text3_y = 500
        game.screen.blit(text3, (text3_x, text3_y))

        text4 = font2.render(
            f'Над игрой для вас работали Антон Лапин и Виктория Дёминова)', True, color1)
        text4_x = 10
        text4_y = 460
        game.screen.blit(text4, (text4_x, text4_y))

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
